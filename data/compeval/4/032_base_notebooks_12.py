def p(g,j=range):
 h,w=len(g),len(g[0])
 for c in j(w):
  u,i=[],0
  for r in j(h):u.append(g[r-h][c])
  u=[0 for x in u if x==0]+[x for x in u if x>0]
  for r in j(h):g[r-h][c]=u[r]
 return g