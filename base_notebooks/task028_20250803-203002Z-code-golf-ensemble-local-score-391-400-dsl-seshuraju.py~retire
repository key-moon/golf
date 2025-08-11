def p(g):
  h, w=len(g), len(g[0])
  points={}
  for r in range(h):
   for c in range(w):
    if g[r][c]!=0:
     points[g[r][c]]=r
  sorted_points=sorted(points.items(), key=lambda item: item[1])
  top_c, bot_c=sorted_points[0][0], sorted_points[1][0]
  res=[[0]*w for _ in range(h)]
  for r in range(5):
   res[r]=[top_c]*w if r in[0, 2]else[top_c]+[0]*(w-2)+[top_c]
  for r in range(5, 10):
   res[r]=[bot_c]*w if r in[7, 9]else[bot_c]+[0]*(w-2)+[bot_c]
  return res
 