import re
p=lambda g,c=-2:g*c or eval(re.sub('1.{5}1(.{25})?'*3,r'0,2,0\1 2,2,2\2 0,2,0\3',str(p(g,c+1))))