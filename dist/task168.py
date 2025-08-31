import re
p=lambda g:eval(r'(g:=[*zip(*eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1\2",str(g)))[::-1])]),'*32)[-1]