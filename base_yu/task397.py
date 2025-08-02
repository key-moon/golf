# def p(g):
#  for i in range(9)[::-1]:
#   for j in range(9):
#    s=[g[i+k%2][j+k//2]for k in range(4)]
#    if all(s):
#     for k in range(len(set(s))):
#      g[i+2+k][j]=g[i+2+k][j+1]=3
#  return g

def p(g):
 for i in range(90):
  if all(s:=[g[k%2+(j:=~i//9)][i%9+k//2]for k in range(4)]):
   for u in g[j+2:][:len({*s})]:
    u[i%9]=u[i%9+1]=3
 return g

# def p(g):
#  for i in range(81):
#    if all(s:=[(u:=g[~i//9-1:])[k%2][i%9+k//2]for k in range(4)]):
#     for v in u[2:2+len(set(s))]:
#      v[i%9]=v[i%9+1]=3
#  return g
