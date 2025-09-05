import re
p=lambda g,c=-11:c*g or[*zip(*eval(re.sub('0(?=, [47].{25}[47])','7',str(p(g,c+1)))))][::-1]