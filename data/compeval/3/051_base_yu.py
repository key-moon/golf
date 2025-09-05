import re
p=lambda g,c=-3:c*g or[*zip(*eval(re.sub('0(?=(, 0)*(, [^0])+(?!\\2), ([^0]), 0)','\\3',str(p(g,c+1)))))][::-1]