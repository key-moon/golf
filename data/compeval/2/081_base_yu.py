import re
p=lambda g,c=-7:c*g or[*zip(*eval(re.sub('0(?=, 8.{19}8)','1',str(p(g,c+1)))))][::-1]