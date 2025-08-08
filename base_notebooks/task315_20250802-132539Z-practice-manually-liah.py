def p(m):
 n=len(m)
 o=[[0]*n*n for _ in range(n*n)]
 for i in range(n):
  for j in range(n):
   if m[i][j]==2:
    for a in range(n):
     for b in range(n):o[i*n+a][j*n+b]=m[a][b]
 return o

