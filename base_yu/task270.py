# best: 116(jailctf merger) / others: 117(ox jam), 120(jacekw Potatoman nauti natte), 120(intgrah jimboko awu macaque sammyuri), 121(jacekw Potatoman nauti), 122(4atj sisyphus luke Seek mukundan)
# ====================================================== 116 =======================================================
# import re;p=lambda g,c=-7:c*g or p([*zip(*eval(r'(g:=eval(re.sub("%d, ((\d, )*)0, %d",r"0,\1 %d,%d",str(g)))),'*2%(3,2,3,2,7,1,7,1))[1][::-1])],c+1)
# port re;p=lambda g,c=-7:c*g or p([*zip(*eval(r'(g:=eval(re.sub("(%d), ((\d, )*)0, (%d)",r"0,\2 \1,\4",str(g)))),'*2%(3,2,7,1))[1][::-1])],c+1)
# port re;p=lambda g,c=-7:c*g or [*zip(*eval(re.sub("([37])([^[(]+)0(, [12])",r"0\2\1\3",str(p(g,c+1)))))][::-1]
# port re;p=lambda g,c=-7:c*g or[*zip(*eval(re.sub("(%s)([^[(]+)0(, %s)"%(3,2,7,1)[c],r"0\2\1\3",str(p(g,c+1)))))][::-1] <- 長そうだから一旦放棄
import re;p=lambda g,c=-7:c*g or[*zip(*eval(re.sub("((3)|7)([^[(]+)0(, (?(2)2|1))",r"0\3\1\4",str(p(g,c+1)))))][::-1]

# import re
# def p(g):
#  for _ in range(4):
#   g=[*zip(*g[::-1])]
#   g=eval(re.sub(r"3, ((\d, )*)0, 2",r"0,\1 3,2",str(g)))
#   g=eval(re.sub(r"7, ((\d, )*)0, 1",r"0,\1 7,1",str(g)))
#  return g
