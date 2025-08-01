def p(g):
 z=list(zip(*g));n=len(g)
 r=max(range(n),key=lambda i:sum(map(bool,g[i])))
 c=z.index(max(z,key=lambda v:sum(map(bool,v))))
 for i in(r-1,r,r+1):
  for j in(c-1,c,c+1):
   if i-r or j-c:
    try:g[i][j]=4
    except:pass
 return g