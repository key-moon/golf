def p(g):
 w=1;c=8
 H=len(g);W=len(g[0]);o=[r[:]for r in g]
 for t in range(w):
  for j in range(W):o[t][j]=o[H-1-t][j]=c
  for i in range(H):o[i][t]=o[i][W-1-t]=c
 return o