import re
p=lambda g,c=-7:c*g or[*zip(*eval(re.sub(r"(([^0]), ([^0]), )0(.{31}\3, )0(.{40})0",r"\1\3\4\2\5\2",str(p(g,c+1))))[::-1])]