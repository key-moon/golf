# best: 150(jailctf merger) / others: 151(4atj sisyphus luke Seek mukundan), 159(ox jam), 176(MasukenSamba), 182(intgrah jimboko awu macaque sammyuri), 189(Afordancja)
# ======================================================================= 150 ========================================================================
def p(g):
 G=sum(g,[])
 u=[c for c in enumerate(G)if c[1]%8]
 while 8in G:
  i=G.index(8)
  for j,v in u:
   G[j]=0
   G[i+j-u[0][0]]=v
 return[G[i*10:][:10]for i in range(10)]

# def p(g):
#  u=[(i,v) for i,v in enumerate(sum(g,[]))if 0<v%8]
#  for i,_ in u:
#   g[i//10][i%10]=0
#  while 8in sum(g,[]):
#   i=sum(g,[]).index(8)
#   for j,v in u:
#    k=i+j-u[0][0]
#    g[k//10][k%10]=v
#  return g
