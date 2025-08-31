import re
p=lambda g,c=3:-c*g or p([*zip(*eval(re.sub('(?<=5, 0.{%d}0, )0'%(len(g)*3-2),str((3<<c)%5),str(g)))[::-1])],c-1)