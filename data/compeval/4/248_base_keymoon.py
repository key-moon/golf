# best: 79(luke, sisyphus) / others: 87(nauti), 93(kabutack), 96(joking+MWI), 96(MeWhenI), 99(MasukenSamba)
# [1,-1][i in(0,len(r)-1)]
# (1-(i in(0,len(r)-1))*2)
# [1,-1][i%(len(r)-1)<1]
# 1-(i%(len(r)-1)<1)*2
# ===================================== 79 ====================================
def p(g,i=0,d=1):
 for r in g[::-1]:r[i]=1;i+=d;d*=1-(i%(len(r)-1)<1)*2
 return g
