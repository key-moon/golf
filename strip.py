import ast
import re
import string

# string.punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
syms = r"=<>!?^|&%()\[\]{},;:*/+-"

ZLIB_GOLF_BANNER = "== begin zlib golf =="

def og_strip(code: str | bytes):
  if isinstance(code, bytes):
    code = code.decode()
  assert isinstance(code, str)
  if ZLIB_GOLF_BANNER in code:
    code = code.split(ZLIB_GOLF_BANNER)[-1]
    lines = [l for l in code.strip().split("\n") if not l.strip().startswith("#") and l.strip()]
    return "\n".join(lines).strip()

  code = re.sub(rf"(\w) *([{syms}])(?!.*['\"])", r"\1\2", code)
  code = re.sub(rf"([{syms}]) *(\w)(?!.*['\"])", r"\1\2", code)
  code = re.sub(rf"([{syms}]) *([{syms}])(?!.*['\"])", r"\1\2", code)
  lines = [l for l in code.strip().split("\n") if not l.strip().startswith("#") and l.strip()]
  if len(lines) == 1: return lines[0]
  res = ""
  basic_indent = min([100]+[len(l) - len(l.lstrip(' ')) for l in lines if l.startswith(" ")])
  if basic_indent == 100: basic_indent = 1
  prev_indent = 0
  for l in lines:
    stripped = l.strip()
    if len(stripped) == 0:
      continue
    indent = (len(l) - len(stripped)) // max(basic_indent, 1)
    if stripped.find("#"):
      stripped = stripped.split("#")[0]

    # 今が if や for、前が if や for、前とindentレベルが違う→一行にまとめない
    if ":" in stripped or ":" in res.split("\n")[-1] or indent != prev_indent:
      res += "\n" + " " * indent + stripped
    else:
      if res and res[-1] != ":": res += ";"
      res += stripped
    prev_indent = indent
  
  return res.strip()

import python_minifier
import sys

import python_minifier.ast_compare

# deflate的には " " が邪魔なことがある。なのですべてのspaceを "\t" にしてしまいたい。
# 文字列リテラル内にある場合は置換できないので、文字列リテラル内にないことを確認してからreplaceする
def get_stripper(prefer_sep="\t", **minifier_opt):
    def strip(source: str | bytes):
        # global 変数が存在するときは、それのrenameはうまくいかない
        # TODO: globalの変数だけ抽出してignoreに入れる（正直複数関数あること最終的にないと思うからなくてもいいと思うけど）
        if isinstance(source, str):
            source = source.encode()
        if b"global" in source:
            _minifier_opt = { **minifier_opt, "rename_globals": False }
        else:
            _minifier_opt = minifier_opt
        source = python_minifier.minify(source, **_minifier_opt)
        # minifierはtab indentationなので、spaceに置き換えて正規化
        source = re.sub(r'^\t+', lambda m: ' ' * len(m.group(0)), source, flags=re.MULTILINE)

        other_sep = { " ": "\t", "\t": " " }[prefer_sep]
        replaced_source = source.replace(other_sep, prefer_sep)
        try:
            python_minifier.ast_compare.compare_ast(ast.parse(source), ast.parse(replaced_source))
            source = replaced_source
        except python_minifier.ast_compare.CompareError:
            pass

        # 数のリテラル周りの切り詰め
        # if, else, for, and, orの前にはspace不要 / forの後にはspace不要
        # orの前が0だとoct literalのパースが走るのでそれだけ注意
        # シンボル名に含まれている場合に死ぬので、雑なチェックで弾く これは rename で A0 みたいな名前が出てくることでおこる
        # すり抜ける場合はあるがゴルフ優先
        #  TODO: 実はもっと削れる可能性はある ( if1: print(1) みたいなのは valid )
        source = re.sub(r'([^ABC][0-9])[ \t]+(in|if|else|for|and)', r'\1\2', source)
        source = re.sub(r'([^ABC][1-9])[ \t]+(or)', r'\1\2', source)
        source = re.sub(r'(for)[ \t]+([0-9])', r'\1\2', source)
        # minifierがバカで for*a,x みたいなのが壊れるののhotfix
        source = re.sub(r'for\(\*([^)]+)\)in', r'for*\1 in', source)
        return source
    return strip

strip = strip_for_plain = get_stripper(
    prefer_sep=" ",
    remove_literal_statements=True,
    remove_asserts=True,
    remove_debug=True,
    # python_minifier の rename は関数内に出てくるsymbolを別のsymbolにリネームする。
    # これによって、"i,j"のようなよく出てくるフレーズが破壊されて圧縮に悪い
    # なので、_と小文字変数に限ってはrenameをしないことにした
    preserve_locals=list("_" + string.ascii_lowercase),
    rename_globals=True,
    preserve_globals=["p"]
)
strip_for_zlib = get_stripper(
    prefer_sep="\t",
    remove_literal_statements=True,
    remove_asserts=True,
    remove_debug=True,
    preserve_locals=list("_" + string.ascii_lowercase),
    rename_globals=False,
    hoist_literals=False,
)
strip_for_zlib_space = get_stripper(
    prefer_sep=" ",
    remove_literal_statements=True,
    remove_asserts=True,
    remove_debug=True,
    preserve_locals=list("_" + string.ascii_lowercase),
    rename_globals=False,
    hoist_literals=False,
)

strippers = {"forcomp-t": strip_for_zlib,"forcomp-s": strip_for_zlib_space,"forplain": strip_for_plain,"raw": og_strip}

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python strip.py <input_file> [mode]")
        sys.exit(1)

    input_file = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "forplain"

    if mode not in strippers:
        print(f"Invalid mode: {mode}. Valid modes are: {', '.join(strippers.keys())}")
        sys.exit(1)

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            source_code = f.read()

        stripper = strippers[mode]
        stripped_code = stripper(source_code)

        print(stripped_code)
    except Exception as e:
        print(f"Error: {e}")
