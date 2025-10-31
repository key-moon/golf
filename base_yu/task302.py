# best: 89(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 91(ox jam), 93(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 93(intgrah jimboko awu macaque sammyuri), 101(HIMAGINE THE FUTURE.), 106(FuunAgent)
# ========================================== 89 =========================================

def p(g,E=enumerate):
 for i,s in E(g):
  for j,t in E(zip(*g)):
   v=[*s[j:],0].index(0)
   w=[*t[i:],0].index(0)
   if(2<w<=v)*(s[j]==5):
    g[i+1][j+1:j-1+v]=[v+3]*(v-2)
 return g
