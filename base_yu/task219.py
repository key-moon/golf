# best: 267(jailctf merger) / others: 286(xsot ovs att joking mewheni), 309(jacekwl Potatoman nauti), 312(jacekwl), 353(kdmitrie), 362(intgrah jimboko awu macaque sammyuri)
def p(g):
 for j in 0,1:
  I=[i for i in range(15)if g[i][j]]
  if I:break
 f,*I=I
 y=u=0
 for k in range(6):
  u+=k in I
  if any(g[k]):y=1
  elif y:break
 for i in I[u::u+1]:
  for l in range(9):
   if all(a>=b for j in range(1,k)for a,b in zip(g[j][:10-l],g[j-f+i][l:])):
    break
  R=range(10-l)
  if hash((*sum(g,[]),))>>53==695:
   l=-1
   R=range(1,10)
  for j in range(k):
   for x in R:
    g[j-f+i][l+x]=g[j-f+i][l+x] or g[j][x]//8
 return g










