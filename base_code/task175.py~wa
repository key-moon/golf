def p(g):
 from collections import Counter
 R,C=len(g),len(g[0])
 for i in range(R):
  for j in range(C):
   if g[i][j]==0:
    c=[g[i+di][j+dj] 
       for di in(-1,0,1) for dj in(-1,0,1)
       if di|dj
       if 0<=i+di<R and 0<=j+dj<C
       if g[i+di][j+dj]]
    m=Counter(c).most_common()
    g[i][j]=m[1][0] if len(m)>1 else m[0][0]
 return g
