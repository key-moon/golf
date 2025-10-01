A=range
def p(g):
 for j in 0,1:
  B=[i for i in A(15)if g[i][j]]
  if B:break
 f,*B=B;y=u=0
 for k in A(6):
  u+=k in B
  if any(g[k]):y=1
  elif y:break
 for i in B[u::u+1]:
  for l in A(9):
   if all(a>=b for j in A(1,k)for(a,b)in zip(g[j][:10-l],g[j-f+i][l:])):break
  C=A(10-l)
  if hash((*sum(g,[]),))>>53==695:l=-1;C=A(1,10)
  for j in A(k):
   for x in C:g[j-f+i][l+x]=g[j-f+i][l+x]or g[j][x]//8
 return g