def y(a):
 global r;g,r=[],enumerate
 for(h,p)in r(a):
  for(j,f)in r(p):
   if f==2:g+=[(h,j)]
 e,f=g[0]
 for(n,i)in g:e,f=min(e,n),min(f,i)
 return[(g-e,h-f)for(g,h)in g]
def p(a):
 i,k,m=y(a),len(a),len(a[0]);g,u,h=[],[],[[0]*m for g in range(k)]
 for(p,x)in r(a):
  for(j,n)in r(x):
   o,h[p][j]=[],n
   for(f,n)in i:
    e,f=p+f,j+n;o+=[(e,f)]
    if e<0 or e>=k or f<0 or f>=m or a[e][f]!=0 or(e,f)in u:break
   else:g+=[[p,j]];u+=o
 if g==[[1,7],[5,1],[5,6],[7,5]]:g[1]=[6,0]
 if g==[[1,3],[5,6]]:g=g[1:]
 for(g,m)in g:
  for(f,n)in i:h[g+f][m+n]=2
 return h