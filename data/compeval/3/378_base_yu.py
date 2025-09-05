import re
p=lambda g,c=-3:c*g or[*zip(*eval(re.sub('0(?=(.{%d}.{4})*.{%d}0, ([1-9]), \\2.{%d}.{%d}.0, ([1-9]))'%((len(g)*3+1,)*4),'\\3',str(p(g,c+1))))[::-1])]