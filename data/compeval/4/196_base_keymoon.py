import re
p=lambda g,c=79:-c*g or[*zip(*eval(re.sub(*[' 0(?=, 0\.|\))','1(?=, 0,|, 3)','0.','3'][c>64::2],str(p(g,c-1)))))][::-1]