from collections import Counter
def p(m):
 n=len(m)
 c=Counter(e for r in m for e in r).most_common(1)[0][0]
 o=[[0]*n*n for _ in range(n*n)]
 for i in range(n):
  for j in range(n):
   if m[i][j]==c:
    for a in range(n):
     for b in range(n):o[i*n+a][j*n+b]=m[a][b]
 return o
