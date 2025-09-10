import re
p=lambda g,c=-7:c*g or[*zip(*eval(re.sub(r"(([^0]), ([^0]), \2, )0(.{31}\2, )0(.{40})0",r"\1\2\4\3\5\3",str(p(g,c+1))))[::-1])]