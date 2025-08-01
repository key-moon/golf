def p(g):
 h,w=len(g),len(g[0]);v=max(map(max,g));u=[[0]*w for _ in g]
 for a in range(h):
  for b in range(a,h):
   for c in range(w):
    for d in range(c,w):
     if all(g[i][j]==v for i in range(a,b+1) for j in range(c,d+1)):
      if not(a and all(g[a-1][j]==v for j in range(c,d+1))or b<h-1 and all(g[b+1][j]==v for j in range(c,d+1))or c and all(g[i][c-1]==v for i in range(a,b+1))or d<w-1 and all(g[i][d+1]==v for i in range(a,b+1))):
       for i in range(a,b+1):
        for j in range(c,d+1):u[i][j]=v
 return u
