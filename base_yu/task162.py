# best: 100(4atj) / others: 104(sisyphus), 107(joking+MWI), 107(joking), 108(mukundan), 110(natte)
# ============================================== 100 ===============================================
# p=lambda g,c=-3:c*g or p([[*map(int,c)]for c in re.sub("000(.{18})000(.{18})000","111\\g<1>111\\g<2>111",re.sub("[[ ,]","",str(g))).split("]")[:-2]],c+1)
# p=lambda g,c=-3:c*g or p(eval(re.sub("0, 0, 0(.{55})0, 0, 0(.{55})0, 0, 0","1,1,1\\1 1,1,1\\2 1,1,1",str(g))),c+1)
import re
# p=lambda g,c=-3:c*g or p(eval(re.sub(("(.{55})0, 0, 0"*3)[7:],"1,1,1\\1 1,1,1\\2 1,1,1",str(g))),c+1)
p=lambda g,c=-3:c*g or p(eval(re.sub("(.{55})?0, 0, 0"*3,r"\1 1,1,1\2 1,1,1\3 1,1,1",str(g))),c+1)
# p=lambda g:eval(r'(g:=eval(re.sub("(.{55})?0, 0, 0"*3,"\\1 1,1,1\\2 1,1,1\\3 1,1,1",str(g)))),'*3)[2]
# p=lambda g,c=-3:c*g or p(eval(re.sub("(.{55})?0, 0, 0"*3," 1,1,1\\".join("01234")[7:-2],str(g))),c+1)
