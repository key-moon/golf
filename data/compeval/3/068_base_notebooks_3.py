def p(g):
 c={}
 q=range
 for i in q(10):
  for j in q(10):
   if g[i][j]:c[g[i][j]]=c.get(g[i][j],0)+1
 a=next(k for k,v in c.items()if v==1)
 b,c=next((i,j)for i in q(10)for j in q(10)if g[i][j]==a)
 r=[[0]*10for _ in q(10)]
 r[b][c]=a
 for e in[-1,0,1]:
  for f in[-1,0,1]:
   if e or f:
    w,x=b+e,c+f
    if 0<=w<10and 0<=x<10:r[w][x]=2
 return r
