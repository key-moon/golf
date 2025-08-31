import ast
import zlib
from compress import compress
import python_minifier
from strip import strip_for_zlib, strip_for_plain, get_stripper
from python_minifier.ast_printer import print_ast

# print(print_ast(ast.parse("if a:=1:1")))

print(python_minifier.minify('b"\\y\1\2\3\4"'))
print(python_minifier.minify('"\x80\xff"'))
print(python_minifier.minify('(a:=1,2)+1'))
print(python_minifier.minify('f(a:=1,2)'))
print(python_minifier.minify('if a:=1:1'))
print(python_minifier.minify('while a:=1:1'))
print(python_minifier.minify('for _ in (a:=[1]):...'))
print(python_minifier.minify('[1][a:=1]'))
print(python_minifier.minify('[a:=1 for _ in (1,2)]'))
print(python_minifier.minify('for i in 1,2:...'))
print(python_minifier.minify('[1 for*a,b in ()]'))
