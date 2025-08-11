def p(g):
 R=range
 h,w=len(g),len(g[0])
 f={}
 for i in R(h):
  for j in R(w):
   if g[i][j]:f[g[i][j]]=f.get(g[i][j],0)+1
 x,y=max(f,key=f.get),min(f,key=f.get)
 m,z=0,None
 for t in R(h-2):
  for l in R(w-2):
   for b in R(t+2,h):
    for r in R(l+2,w):
     if all(g[t][j]==x for j in R(l,r+1))and all(g[b][j]==x for j in R(l,r+1))and all(g[i][l]==x for i in R(t,b+1))and all(g[i][r]==x for i in R(t,b+1)):
      a=(b-t+1)*(r-l+1)
      if a>m:m,z=a,(t,l,b,r)
 t,l,b,r=z
 return[[y if g[t+i][l+j]==x else g[t+i][l+j]for j in R(r-l+1)]for i in R(b-t+1)]
