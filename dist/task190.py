import re
p=lambda g,c=-39:c*g or p([*zip(*eval(re.sub("(([1-9]), (\\2.{34}){2,})0","\\1\\2",str(g)))[::-1])],c+1)