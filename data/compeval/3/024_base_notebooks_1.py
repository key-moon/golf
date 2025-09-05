def p(g):
  h, w=len(g), len(g[0])
  res=[[0]*w for _ in range(h)]       
  for c in range(w):
   if any(g[r][c]==2 for r in range(h)):
    for r in range(h):
     res[r][c]=2        
  for r in range(h):
   row_colors=sorted([x for x in set(g[r])if x not in[0, 2]], reverse=True)
   if row_colors:
    res[r]=[row_colors[0]]*w                
  return res
 