import ast
import builtins
import sys
from io import StringIO
from typing import Any
import re
import strip

RESERVED = {"True", "False", "None", "p"} | set(dir(builtins))

# exec 文字列の解析と、関数呼び出しのキーワード「c=」の c を通常の出現と同様に数える対応を含む
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

    # 文字列トークン先頭から内容開始位置までの長さ
    _str_head_re = re.compile(r"""(?ix)
        (?:[rubf]{0,3})
        (?P<q>'''|""" + '"""' + r"""|'|")
    """)
    def string_content_offset_in_token(token_src: str) -> int:
        m = _str_head_re.match(token_src)
        return 0 if not m else len(m.group(0))

    # 文字列トークンの末尾クォート長
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

    # exec 引数式を静的評価し内側コード断片のリストへ
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

        # 乗算 "..." * N または N * "..."
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            # 左が文字列
            if isinstance(node.left, ast.AST) and isinstance(node.right, ast.Constant) and isinstance(node.right.value, int):
                n = node.right.value
                if n <= 0:
                    return []
                segs = eval_exec_arg_to_segments(node.left)
                return segs * n
            # 右が文字列
            if isinstance(node.right, ast.AST) and isinstance(node.left, ast.Constant) and isinstance(node.left.value, int):
                n = node.left.value
                if n <= 0:
                    return []
                segs = eval_exec_arg_to_segments(node.right)
                return segs * n

        # 括弧など
        if isinstance(node, ast.Expr):
            return eval_exec_arg_to_segments(node.value)

        # 静的評価不可
        return []

    # キーワード名の直近の一致位置をオフセットで取得
    _kw_pattern_cache: dict[str, re.Pattern] = {}
    def _last_kw_name_offset_between(src_text: str, name: str, abs_start: int, abs_end: int) -> int | None:
        seg = src_text[abs_start:abs_end]
        pat = _kw_pattern_cache.get(name)
        if pat is None:
            pat = re.compile(rf"\b({re.escape(name)})\s*=")
            _kw_pattern_cache[name] = pat
        m_last = None
        for m in pat.finditer(seg):
            m_last = m
        if m_last is None:
            return None
        return abs_start + m_last.start(1)

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
            # まず通常走査
            self.generic_visit(node)

            # キーワード引数名も出現としてカウント
            if node.keywords:
                call_abs_start = to_offset(getattr(node, "lineno", 1), getattr(node, "col_offset", 0))
                for kw in node.keywords:
                    if kw.arg is None:
                        continue  # **kwargs
                    name = kw.arg
                    if name in RESERVED:
                        continue
                    # 値の直前までを走査して name\s*= を後方一致
                    val_abs_start = to_offset(kw.value.lineno, kw.value.col_offset)
                    occ = _last_kw_name_offset_between(src, name, call_abs_start, val_abs_start)
                    if occ is not None:
                        out.append({"name": name, "lineno": 1, "col_offset": occ, "_absolute": True})

            # exec の内部コードも解析
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
                            "_absolute": True,
                        })

    Visitor().visit(tree)

    # ここから追加: 極大 [A-Za-z_]+ の字句列を列挙し、[A-Z]+ のみを強制変数として追加
    # コメントや文字列も含む src 全体を対象
    UWORD = re.compile(r"[A-Za-z_]+")
    forced_upper: dict[str, list[int]] = {}
    for m in UWORD.finditer(src):
        tok = m.group(0)
        # 大文字のみで構成されるかを ASCII 基準で判定
        if re.fullmatch(r"[A-Z]+", tok) and tok not in RESERVED:
            forced_upper.setdefault(tok, []).append(m.start())

    # 変数名ごとにオフセット集約
    var_dict: dict[str, list[int]] = {}
    for item in out:
        name = item["name"]
        if name in RESERVED:
            continue
        off = item["col_offset"] if item.get("_absolute") else to_offset(item["lineno"], item["col_offset"])
        var_dict.setdefault(name, []).append(off)

    # 強制追加分をマージ
    for name, offs in forced_upper.items():
        var_dict.setdefault(name, []).extend(offs)

    result = [{"name": name, "occurrences": sorted(set(pos))} for name, pos in sorted(var_dict.items())]

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
        raw = b"def p(i):\n exec('l,e=-e,l;i[g+l>>1][d+e>>1]=a;'*3)\n# CONST ALPHA Beta _X\n"
    print(list_var_occurrences(raw, as_text=True, include_exec=True), end="")
