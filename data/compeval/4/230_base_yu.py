import re
p=lambda g,c=3:-c*g or[*zip(*eval(re.sub('0(?=, 0,.{%s}5, 5)'%len(g*3),'3**c%5',str(p(g,c-1))))[::-1])]