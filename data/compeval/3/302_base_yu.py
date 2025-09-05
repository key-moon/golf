# best: 97(mukundan) / others: 100(joking+MWI), 101(joking), 104(Seek64), 152(biz), 187(MeWhenI)
# ============================================== 97 =============================================

def p(g,E=enumerate):
 for i,s in E(g):
  for j,t in E(zip(*g)):
   v=[*s[j:],0].index(0)
   w=[*t[i:],0].index(0)
   if(2<w<=v)*(s[j]==5):
    g[i+1][j+1:j-1+v]=[v+3]*(v-2)
 return g
