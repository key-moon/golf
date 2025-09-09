# best: 89(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 93(xsot ovs att joking mewheni), 97(mukundan), 112(biz), 118(intgrah jimboko awu macaque sammyuri), 142(Afordancja)
# ========================================== 89 =========================================

def p(g,E=enumerate):
 for i,s in E(g):
  for j,t in E(zip(*g)):
   v=[*s[j:],0].index(0)
   w=[*t[i:],0].index(0)
   if(2<w<=v)*(s[j]==5):
    g[i+1][j+1:j-1+v]=[v+3]*(v-2)
 return g
