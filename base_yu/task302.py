# best: 89(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 93(ox jam), 102(intgrah jimboko awu macaque sammyuri), 109(import itertools), 109(Tony Li & Darren Amadeus Martin), 112(2F)
# ========================================== 89 =========================================

def p(g,E=enumerate):
 for i,s in E(g):
  for j,t in E(zip(*g)):
   v=[*s[j:],0].index(0)
   w=[*t[i:],0].index(0)
   if(2<w<=v)*(s[j]==5):
    g[i+1][j+1:j-1+v]=[v+3]*(v-2)
 return g
