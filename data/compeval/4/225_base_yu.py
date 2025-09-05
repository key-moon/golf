import re
p=lambda g,c=-15:c*g or[*zip(*eval(re.sub('(0.{16}0, ([^0]), (?!\\2|0).{43}(...)?(.{20})?)0',r'\1\2',str(p(g,c+1))))[::-1])]