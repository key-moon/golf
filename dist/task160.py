import re
p=lambda g:eval(r'(g:=eval(re.sub("1, 1, 1(.{25})1, 0, 1(.{25})1, 1, 1",r"0,2,0\1 2,2,2\2 0,2,0",str(g)))),'*2)[1]