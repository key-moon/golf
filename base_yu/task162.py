# best: 96(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 97(jailctf merger), 101(ox jam), 105(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 105(biz), 109(import itertools)
# ============================================= 96 =============================================
# p=lambda g,c=-3:c*g or p([[*map(int,c)]for c in re.sub("000(.{18})000(.{18})000","111\\g<1>111\\g<2>111",re.sub("[[ ,]","",str(g))).split("]")[:-2]],c+1)
# p=lambda g,c=-3:c*g or p(eval(re.sub("0, 0, 0(.{55})0, 0, 0(.{55})0, 0, 0","1,1,1\\1 1,1,1\\2 1,1,1",str(g))),c+1)
# port re;p=lambda g,c=-3:c*g or p(eval(re.sub(("(.{55})0, 0, 0"*3)[7:],"1,1,1\\1 1,1,1\\2 1,1,1",str(g))),c+1)
# port re;p=lambda g:eval(r'(g:=eval(re.sub("(.{55})?0, 0, 0"*3,"\\1 1,1,1\\2 1,1,1\\3 1,1,1",str(g)))),'*3)[2]
# port re;p=lambda g,c=-3:c*g or p(eval(re.sub("(.{55})?0, 0, 0"*3," 1,1,1\\".join("01234")[7:-2],str(g))),c+1)
# port re;p=lambda g,c=-3:c*g or p(eval(re.sub("(.{55})?0, 0, 0"*3,rf"\1{(a:=' 1,1,1')}\2{a}\3{a}",str(g))),c+1)
# port re;p=lambda g,c=-3:c*g or p(eval(re.sub("(.{55})?0, 0, 0"*3,rf"\1 1,1,1\2 1,1,1\3 1,1,1",str(g))),c+1)
import re;p=lambda g,c=-3:c*g or p(eval(re.sub("(.{55})?0, 0, 0"*3,r"\%s 1,1,1"*3%(*"123",),str(g))),c+1)
