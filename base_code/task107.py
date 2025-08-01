def p(g):
 n=len(g);k=len({*sum(g,[])})-1;o=[[0]*n*k for _ in range(n*k)]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:
    for a in range(k):o[i*k+a][j*k:j*k+k]=[v]*k
 for b in range(n):
  for a in range(k):
   i=b*k+a
   if not o[i][i]:o[i][i]=2
   j=(n-1-b)*k+k-1-a
   if not o[i][j]:o[i][j]=2
 return o
