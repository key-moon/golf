import re
p=lambda g,c=-7:c*g or[*zip(*eval(re.sub('((3)|7)([^[(]+)0(, (?(2)2|1))',r'0\3\1\4',str(p(g,c+1)))))][::-1]