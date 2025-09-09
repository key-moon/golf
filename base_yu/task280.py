# best: 179(4atj sisyphus luke Seek mukundan) / others: 182(xsot ovs att joking mewheni), 185(jailctf merger), 210(intgrah jimboko awu macaque sammyuri), 241(Potatoman), 241(jacekwl Potatoman nauti)
# ====================================================================================== 179 ======================================================================================
def p(g):
 o=[s[:]for s in g]
 for f in range(4):
  for i in range(len(g)-1):
   for j in range(len(g)):
    if g[i+1][j]<g[i][j]<3:
     for k in range(9):
      if g[i-k][j]<1:break
     for s in o[i:]:
      s[j-k+1:j+k]=g[i][j-k+1:j+k]
  *g,=zip(*g[::-1])
  *o,=map(list,zip(*o[::-1]))
 return o





