def p(g):
 val_n,val_m=len(g),len(g[0])
 # pick the two non‐zero border colours
 bc={*g[0],*g[-1],*(r[0] for r in g),*(r[-1] for r in g)}-{0}
 c1,c2=bc
 # find first switch‐row on left/right from c1→c2
 for i in range(1,val_n):
  if g[i][0]!=c1: r1=i;break
 for i in range(1,val_n):
  if g[i][-1]!=c1: r2=i;break
 # find first switch‐col on top/bottom from c2→c1
 for j in range(1,val_m):
  if g[0][j]!=c2: c3=j;break
 for j in range(1,val_m):
  if g[-1][j]!=c2: c4=j;break
 # fill all zeros in that interior rect
 for i in range(min(r1,r2),max(r1,r2)+1):
  for j in range(min(c3,c4),max(c3,c4)+1):
   if g[i][j]==0:g[i][j]=3
 return g
