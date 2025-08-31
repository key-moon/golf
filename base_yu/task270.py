# best: 119(xsot ovs att joking mewheni) / others: 130(jailctf merger), 131(mukundan), 135(4atj sisyphus luke Seek), 168(MasukenSamba), 222(jacekwl)
# ======================================================== 119 ========================================================
import re;p=lambda g,c=-7:c*g or p([*zip(*eval(r'(g:=eval(re.sub("%d, ((\d, )*)0, %d",r"0,\1 %d,%d",str(g)))),'*2%(3,2,3,2,7,1,7,1))[1][::-1])],c+1)

# import re
# def p(g):
#  for _ in range(4):
#   g=[*zip(*g[::-1])]
#   g=eval(re.sub(r"3, ((\d, )*)0, 2",r"0,\1 3,2",str(g)))
#   g=eval(re.sub(r"7, ((\d, )*)0, 1",r"0,\1 7,1",str(g)))
#  return g
