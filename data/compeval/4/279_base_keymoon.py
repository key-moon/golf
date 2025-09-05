import re
p=lambda g,c=79:-c*g or[*zip(*eval(re.sub(*['9(?=, 9\.|\))','1(?=, 9,|, 8)','9.','8'][c>64::2],str(p(g,c-1)))))][::-1]