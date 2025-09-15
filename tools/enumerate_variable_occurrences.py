import ast
import builtins
import sys
from io import StringIO
from typing import Any
import strip

RESERVED = {"True", "False", "None", 'p'} | set(dir(builtins))

def list_var_occurrences(code: str, as_text = False):
    """
    code 中の変数名の全出現を抽出する
    - ast.Name を基本に収集する
    - 関数定義のパラメータ ast.arg も収集する
    戻り値は name lineno col_offset end_lineno end_col_offset role を持つ辞書の配列
    """
    code = strip.strip_for_zlib(code).encode()
    tree = ast.parse(code)

    out: list[dict[str, Any]] = []

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node: ast.Name) -> Any:
            # 属性アクセス obj.attr の attr は ast.Attribute に保持されるためここでは来ない
            if node.id not in RESERVED:
                out.append({
                    "name": node.id,
                    "lineno": node.lineno,
                    "col_offset": node.col_offset,
                    "end_lineno": getattr(node, "end_lineno", node.lineno),
                    "end_col_offset": getattr(node, "end_col_offset", node.col_offset + len(node.id)),
                    "role": type(node.ctx).__name__,  # Load Store Del
                })
            self.generic_visit(node)

        def visit_arg(self, node: ast.arg) -> Any:
            # 関数定義のパラメータ
            if node.arg not in RESERVED:
                out.append({
                    "name": node.arg,
                    "lineno": node.lineno,
                    "col_offset": node.col_offset,
                    "end_lineno": getattr(node, "end_lineno", node.lineno),
                    "end_col_offset": getattr(node, "end_col_offset", node.col_offset + len(node.arg)),
                    "role": "Param",
                })
            self.generic_visit(node)

        # except e の e は Python 3.11 では名前が文字列で位置情報を持たないため除外
        # match 文の束縛名も同様に位置を厳密に取得できないため除外

    Visitor().visit(tree)

    def lineno_and_col_to_offset(lineno: int, col: int) -> int:
        lines = code.splitlines(keepends=True)
        offset = sum(len(lines[i]) for i in range(lineno - 1)) + col
        return offset

    # 変数名ごとにdictを作り、(lineno, col_offset) の組をdict要素の配列にする（ソートもする）
    var_dict = {}
    for item in out:
        var_dict.setdefault(item["name"], []).append(lineno_and_col_to_offset(item["lineno"], item["col_offset"]))
    out = []
    for name, items in var_dict.items():
        items.sort()
        out.append({
            "name": name,
            "occurrences": items,
        })
    out.sort(key=lambda x: x["name"])
    if as_text:
        buf = StringIO()
        buf.write(f'{len(out)}\n')
        for item in out:
            name = item["name"]
            occurrences = item["occurrences"]
            buf.write(f'{name} {len(occurrences)}\n')
            buf.write(' '.join(map(str, occurrences)) + '\n')
        return buf.getvalue()
    else:
        return out


if __name__ == "__main__":

    # load from sys argv[1] or stdin (--input)
    if len(sys.argv) == 2:
        if sys.argv[1] == "--input":
            sample = sys.stdin.read()
        else:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                sample = f.read()
    else:
        print('Usage: python enumerate_variable_occurrences.py [--input | <filename>]', file=sys.stderr)
        print('Executing sample code...', file=sys.stderr)
        sample = 'p=lambda g,c=15,d=8:-c*g or[(l:=0)or[l:=v and[-59%v.bit_count()%3,v|l|(v<9)*(d:=d*2)][c<15]for v in s]for s in zip(*p(g,c-1))][::-1]'
        print('Sample code:', sample, file=sys.stderr)

    print(list_var_occurrences(sample, as_text=True), end='')
