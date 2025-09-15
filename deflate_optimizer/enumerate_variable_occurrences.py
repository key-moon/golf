import ast
import builtins
import sys
from io import StringIO
from typing import Any
import re
import strip

RESERVED = {"True", "False", "None", "p"} | set(dir(builtins))

# ChatGPTくんが気合でexec対応してくれました
# https://chatgpt.com/share/68c7f62b-e994-8001-877c-466ce905db7a
def list_var_occurrences(code: bytes | str, as_text: bool = False, nostrip: bool = False,
                         include_attrs: bool = False, include_exec: bool = False):
    if isinstance(code, bytes):
        code = code.decode("utf-8", errors="replace")
    src = strip.strip_for_zlib(code) if not nostrip else code
    tree = ast.parse(src)

    out: list[dict[str, Any]] = []

    lines = src.splitlines(keepends=True)
    def to_offset(ln: int, col: int) -> int:
        return sum(len(lines[i]) for i in range(ln - 1)) + col

    # 文字列トークンのコンテンツ開始相対位置を返す
    _str_head_re = re.compile(r"""(?ix)
        (?:[rubf]{0,3})       # 接頭辞
        (?P<q>'''|""" + '"""' + r"""|'|")  # クォート
    """)
    def string_content_offset_in_token(token_src: str) -> int:
        m = _str_head_re.match(token_src)
        return 0 if not m else len(m.group(0))

    def string_tail_len_from_token(token_src: str, content_rel: int) -> int:
        q3 = token_src[content_rel-3:content_rel]
        if q3 in ("'''", '"""'):
            return 3
        q1 = token_src[content_rel-1:content_rel]
        return 1 if q1 in ("'", '"') else 0

    def find_func_name_col(lineno: int, name: str) -> int | None:
        line = lines[lineno - 1] if 1 <= lineno <= len(lines) else ""
        m = re.search(rf"""\b(?:async\s+)?def\s+({re.escape(name)})\s*(?=\()""", line)
        return None if not m else m.start(1)

    # exec 引数式を静的評価し、「(内部コード文字列, 内部コードの絶対開始オフセット)」のリストへ
    def eval_exec_arg_to_segments(node: ast.AST) -> list[tuple[str, int]]:
        # 文字列定数
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            token_src = ast.get_source_segment(src, node)
            if token_src is None:
                return []
            token_abs = to_offset(node.lineno, node.col_offset)
            content_rel = string_content_offset_in_token(token_src)
            tail = string_tail_len_from_token(token_src, content_rel)
            inner_src = token_src[content_rel:len(token_src)-tail]
            content_abs = token_abs + content_rel
            return [(inner_src, content_abs)]

        # 加算
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            left = eval_exec_arg_to_segments(node.left)
            right = eval_exec_arg_to_segments(node.right)
            return left + right

        # 乗算（"..." * N または N * "..."）
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            # 左が文字列
            if isinstance(node.left, ast.AST) and isinstance(node.right, ast.Constant) and isinstance(node.right.value, int):
                n = node.right.value
                if n <= 0:
                    return []
                segs = eval_exec_arg_to_segments(node.left)
                # 反復は同じオフセットに写像する
                return segs * n
            # 右が文字列
            if isinstance(node.right, ast.AST) and isinstance(node.left, ast.Constant) and isinstance(node.left.value, int):
                n = node.left.value
                if n <= 0:
                    return []
                segs = eval_exec_arg_to_segments(node.right)
                return segs * n

        # 括弧など（再帰させる）
        if isinstance(node, ast.Expr):
            return eval_exec_arg_to_segments(node.value)

        # 静的に評価できないものは無視
        return []

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node: ast.Name) -> Any:
            if node.id not in RESERVED:
                out.append({"name": node.id, "lineno": node.lineno, "col_offset": node.col_offset})
            self.generic_visit(node)

        def visit_arg(self, node: ast.arg) -> Any:
            if node.arg not in RESERVED:
                out.append({"name": node.arg, "lineno": node.lineno, "col_offset": node.col_offset})
            self.generic_visit(node)

        def visit_Attribute(self, node: ast.Attribute) -> Any:
            if include_attrs and node.attr not in RESERVED:
                pass
            self.generic_visit(node)

        def _visit_func_like(self, node: ast.AST, name: str) -> Any:
            if name not in RESERVED:
                col = find_func_name_col(getattr(node, "lineno", 1), name)
                if col is not None:
                    out.append({"name": name, "lineno": node.lineno, "col_offset": col})
            self.generic_visit(node)

        def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
            self._visit_func_like(node, node.name)

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> Any:
            self._visit_func_like(node, node.name)

        def visit_Call(self, node: ast.Call) -> Any:
            # まず通常の走査
            self.generic_visit(node)
            if not include_exec:
                return
            if not (isinstance(node.func, ast.Name) and node.func.id == "exec" and node.args):
                return

            segments = eval_exec_arg_to_segments(node.args[0])
            if not segments:
                return

            # 各セグメントを独立に解析し、オフセットを外側へ射影
            for inner_src, content_abs in segments:
                try:
                    inner_res = list_var_occurrences(inner_src, as_text=False, nostrip=True,
                                                     include_attrs=include_attrs, include_exec=False)
                except Exception:
                    continue
                for item in inner_res:
                    for off in item["occurrences"]:
                        out.append({
                            "name": item["name"],
                            "lineno": 1,
                            "col_offset": content_abs + off,
                            "_absolute": True,  # 既に絶対オフセット
                        })

    Visitor().visit(tree)

    # 変数名ごとにオフセット集約
    var_dict: dict[str, list[int]] = {}
    for item in out:
        off = item["col_offset"] if item.get("_absolute") else to_offset(item["lineno"], item["col_offset"])
        var_dict.setdefault(item["name"], []).append(off)

    result = [{"name": name, "occurrences": sorted(pos)} for name, pos in sorted(var_dict.items())]

    if as_text:
        buf = StringIO()
        buf.write(f"{len(result)}\n")
        for item in result:
            buf.write(f'{item["name"]} {len(item["occurrences"])}\n')
            buf.write(" ".join(map(str, item["occurrences"])) + "\n")
        return buf.getvalue()
    return result


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "--input":
            raw = sys.stdin.buffer.read()
        else:
            with open(sys.argv[1], "rb") as f:
                raw = f.read()
    else:
        raw = b"def p(i):\n exec('l,e=-e,l;i[g+l>>1][d+e>>1]=a;'*3)\n"
    print(list_var_occurrences(raw, as_text=True, include_exec=True), end="")
