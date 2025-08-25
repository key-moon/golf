import re
p=lambda g,c=-3:c*g or p(eval(re.sub("(.{55})?0, 0, 0"*3,"\\1 1,1,1\\2 1,1,1\\3 1,1,1",str(g))),c+1)