def p(g):
 q=range
 r=[o[:]for o in g]
 m,n=len(g),len(g[0])
 p=[(i,j)for i in q(m)for j in q(n)if g[i][j]==8]
 for i,j in p:
  for w,x in[(0,1),(1,0),(0,-1),(-1,0)]:
   k=1
   while 0<=i+k*w<m and 0<=j+k*x<n:
    if g[i+k*w][j+k*x]==8:
     for t in q(1,k):r[i+t*w][j+t*x]=3
     break
    k+=1
 return r