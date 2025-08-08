import ast
import re
import string

# string.punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
# syms = r"=<>!?^|&%()\[\]{},;:*/+-"

# def strip(code: str):
#   matches = sorted(set(re.findall(r'val_[\w_]+', code)))

#   vals = [f"{a}{b}" for a in string.ascii_uppercase[::-1] for b in string.ascii_uppercase[::-1]] + list(string.ascii_uppercase[::-1])
#   for replace in matches:
#     assert len(vals) != 0, "auto variable resolution failed"
#     val_name = vals.pop()
#     while val_name in code:
#       val_name = vals.pop()
#     code = code.replace(replace, val_name)

#   code = re.sub(rf"(\w) *([{syms}])", r"\1\2", code)
#   code = re.sub(rf"([{syms}]) *(\w)", r"\1\2", code)
#   code = re.sub(rf"([{syms}]) *([{syms}])", r"\1\2", code)

#   lines = [l for l in code.strip().splitlines() if not l.strip().startswith("#") and l.strip()]
#   if len(lines) == 1: return lines[0]
#   res = ""
#   basic_indent = min([100]+[len(l) - len(l.lstrip(' ')) for l in lines if l.startswith(" ")])
#   if basic_indent == 100: basic_indent = 1
#   prev_indent = 0
#   for l in lines:
#     stripped = l.strip()
#     if len(stripped) == 0:
#       continue
#     indent = (len(l) - len(stripped)) // max(basic_indent, 1)
#     if stripped.find("#"):
#       stripped = stripped.split("#")[0]

#     # 今が if や for、前が if や for、前とindentレベルが違う→一行にまとめない
#     if ":" in stripped or ":" in res.split("\n")[-1] or indent != prev_indent:
#       res += "\n" + " " * indent + stripped
#     else:
#       if res and res[-1] != ":": res += ";"
#       res += stripped
#     prev_indent = indent
  
#   return res.strip()

import python_minifier
import sys

def get_stripper(**minifier_opt):
    def strip(source: str):
        source = python_minifier.minify(source, **minifier_opt)
        # if, else, for, and, orの前にはspace不要 / forの後にはspace不要
        # orの前が0だとoct literalのパースが走るのでそれだけ注意
        # TODO: 実はもっと削れる可能性はある ( if1: print(1) みたいなのは valid )
        source = re.sub(r'([0-9])[ \t]+(if|else|for|and)', r'\1\2', source)
        source = re.sub(r'([1-9])[ \t]+(or)', r'\1\2', source)
        source = re.sub(r'(for)[ \t]+([0-9])', r'\1\2', source)
        return source.replace("\t", " ")
    return strip

strip = strip_for_plain = get_stripper(
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
    remove_literal_statements=True,
    remove_asserts=True,
    remove_debug=True,
    preserve_locals=list("_" + string.ascii_lowercase),
    rename_globals=False,
    hoist_literals=False,
)

strippers = {"forcompress": strip_for_zlib,"forplain": strip_for_plain}

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
