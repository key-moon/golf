def p(g):
 r=[x[:]for x in g]
 n,m=len(g),len(g[0])
 for i in range(n):
  for j in range(m):
   if g[i][j]==3:
    for d,e in[(0,1),(1,0),(0,-1),(-1,0)]:
     if 0<=i+d<n and 0<=j+e<m and g[i+d][j+e]==3:
      r[i][j]=8
      break
 return r