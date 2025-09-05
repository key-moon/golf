def p(g):
 M,N=len(g),len(g[0])
 S={(i,j)for i in range(M)for j in range(N)if g[i][j]==2}
 while S:
  i,j=S.pop();a=b=i;c=d=j;T=[(i,j)]
  while T:
   x,y=T.pop()
   for u,v in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
    if(u,v)in S:
     S.remove((u,v));T.append((u,v))
     if u<a:a=u
     elif u>b:b=u
     if v<c:c=v
     elif v>d:d=v
  if b>a or d>c:
   for x in range(a-1,b+2):
    if 0<=x<M:
     for y in range(c-1,d+2):
      if 0<=y<N and g[x][y]==0 and (x<a or x>b or y<c or y>d):g[x][y]=3
 return g
