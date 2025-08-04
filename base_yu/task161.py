R=range
def p(g):
 h,w=len(g),len(g[0])
 _,c=max((sum(.5-(0<i<h-1 and 0<j<w-1) for j in R(w)for i in R(h)if g[i][j]==c),c)for c in R(1,10))
 u=[w*[(g[i][0]==c)*c]for i in R(h)]
 for i in R(w):
  for j in R(h*(g[0][i]==c)):u[j][i]=c
 return u

# def p(g):
#  h,w=len(g),len(g[0])
#  _,c=max((sum(.5-(0<i<h-1 and 0<j<w-1) for j in range(w) for i in range(h) if g[i][j]==c),c) for c in range(1,10))
#  u=[[[0,c][g[i][0]==c]]*w for i in range(h)]
#  for i in range(w):
#   if g[0][i]==c:
#    for j in range(h):
#     u[j][i]=c
#  return u