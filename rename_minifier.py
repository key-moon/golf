#!/usr/bin/env python3
import argparse
import ast
import sys
from collections import OrderedDict

# 置き換えに使う文字のリスト：A-Z, a-z, chr(192)～chr(320) ただし215 (×), 247 (÷)は除外
_ALPHABET = (
    [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    + [chr(i) for i in range(ord("a"), ord("z") + 1)]
    + [chr(i) for i in range(192, 321) if i not in (215, 247)]
)


class _NameCollector(ast.NodeVisitor):
    """
    1つの FunctionDef ノード内をスキャンし、
    引数・代入・ループ変数・ラムダ引数・内包表記変数など
    関数内で束縛されるすべての名前をソース順に収集する。
    """
    def __init__(self):
        self.names = []
        self._seen = set()

    def _add(self, name):
        if name not in self._seen:
            self._seen.add(name)
            self.names.append(name)

    def _collect_targets(self, node):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            self._add(node.id)
        elif isinstance(node, (ast.Tuple, ast.List)):
            for elt in node.elts:
                self._collect_targets(elt)
        elif isinstance(node, ast.Starred):
            self._collect_targets(node.value)

    def visit_FunctionDef(self, node):
        # 引数
        for arg in node.args.args:
            self._add(arg.arg)
        if node.args.vararg:
            self._add(node.args.vararg.arg)
        if node.args.kwarg:
            self._add(node.args.kwarg.arg)
        # 本文を再帰
        for stmt in node.body:
            self.visit(stmt)

    def visit_Assign(self, node):
        for tgt in node.targets:
            self._collect_targets(tgt)
        self.generic_visit(node.value)

    def visit_AnnAssign(self, node):
        self._collect_targets(node.target)
        if node.value:
            self.generic_visit(node.value)

    def visit_AugAssign(self, node):
        self._collect_targets(node.target)
        self.generic_visit(node.value)

    def visit_For(self, node):
        self._collect_targets(node.target)
        self.generic_visit(node.iter)
        for stmt in node.body:
            self.visit(stmt)
        for stmt in node.orelse:
            self.visit(stmt)

    def visit_comprehension(self, node):
        self._collect_targets(node.target)
        self.generic_visit(node.iter)
        for if_ in node.ifs:
            self.visit(if_)

    def visit_Lambda(self, node):
        for arg in node.args.args:
            self._add(arg.arg)
        if node.args.vararg:
            self._add(node.args.vararg.arg)
        if node.args.kwarg:
            self._add(node.args.kwarg.arg)
        self.generic_visit(node.body)

    def visit_NamedExpr(self, node):
        self._collect_targets(node.target)
        self.generic_visit(node.value)


class _RenameTransformer(ast.NodeTransformer):
    """
    各 FunctionDef ごとに _NameCollector で作ったマッピングを適用して
    arg.arg と Name.id を置き換える。
    """
    def __init__(self):
        super().__init__()
        self._mapping_stack = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        collector = _NameCollector()
        collector.visit(node)
        mapping = OrderedDict()
        for i, name in enumerate(collector.names):
            if i < len(_ALPHABET):
                mapping[name] = _ALPHABET[i]
        self._mapping_stack.append(mapping)
        for arg in node.args.args:
            if arg.arg in mapping:
                arg.arg = mapping[arg.arg]
        if node.args.vararg and node.args.vararg.arg in mapping:
            node.args.vararg.arg = mapping[node.args.vararg.arg]
        if node.args.kwarg and node.args.kwarg.arg in mapping:
            node.args.kwarg.arg = mapping[node.args.kwarg.arg]
        self.generic_visit(node)
        self._mapping_stack.pop()
        return node

    def visit_Lambda(self, node: ast.Lambda):
        mapping = self._mapping_stack[-1] if self._mapping_stack else {}
        for arg in node.args.args:
            if arg.arg in mapping:
                arg.arg = mapping[arg.arg]
        if node.args.vararg and node.args.vararg.arg in mapping:
            node.args.vararg.arg = mapping[node.args.vararg.arg]
        if node.args.kwarg and node.args.kwarg.arg in mapping:
            node.args.kwarg.arg = mapping[node.args.kwarg.arg]
        node.body = self.visit(node.body)
        return node

    def visit_Name(self, node: ast.Name):
        if self._mapping_stack:
            mapping = self._mapping_stack[-1]
            if node.id in mapping:
                return ast.copy_location(ast.Name(id=mapping[node.id], ctx=node.ctx), node)
        return node


def main():
    parser = argparse.ArgumentParser(
        description="各関数の引数とローカル変数を一文字変数名に置き換えて出力します。"
    )
    parser.add_argument("filepath", help="処理対象の Python ファイルパス")
    args = parser.parse_args()

    try:
        source = open(args.filepath, "r", encoding="utf-8").read()
    except Exception as e:
        sys.exit(f"ファイル読み込みエラー: {e}")

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        sys.exit(f"構文解析エラー: {e}")

    transformer = _RenameTransformer()
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)

    try:
        output = ast.unparse(new_tree)
    except AttributeError:
        sys.exit("このスクリプトは Python 3.9 以上が必要です。")

    print(output)

if __name__ == "__main__":
    main()
