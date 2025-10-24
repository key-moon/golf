# best: 72(jailctf merger) / others: 73(biz), 74(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 74(ox jam), 76(kambarakun), 77(import itertools)
# [1,-1][i in(0,len(r)-1)]
# (1-(i in(0,len(r)-1))*2)
# [1,-1][i%(len(r)-1)<1]
# 1-(i%(len(r)-1)<1)*2
# ================================= 72 =================================
def p(g,i=0,d=1):
 for r in g[::-1]:r[i]=1;i+=d;d*=1-(i%(len(r)-1)<1)*2
 return g
