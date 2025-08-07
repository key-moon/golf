def p(g):
 b=(g[0][0]-1 or g[0][2]-1)+1
 for _ in[0]*4:
  h,w=len(g),len(g[0])
  for i in range(h*w):
   c=g[i%h][i//h];G=[k for k in range(w)if g[i%h][k]not in(c,b)]
   if(c!=b)*(len(G)>2):g[i%h][i//h:G[0]]=[c]*(G[0]-i//h)
  *g,=map(list,zip(*g[::-1]))
 return g