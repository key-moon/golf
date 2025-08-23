R=range(10)
def p(g):
 for _ in[0]*4:
  for i in R:
   if{*g[i]}=={0,2}and{*g[i+1]}>{0}:g=[[v or 3 for v in(j<=i)*(i*2+1-j<10)and g[i*2+1-j]or g[j]]for j in R]
  *g,=zip(*g[::-1])
 return g

# R=range(10)
# def p(g):
#  for _ in[0]*4:
#   for i in R:
#    if{*g[i]}=={0,2}and{*g[i+1]}!={0}:g=[[v or 3 for v in(j<=i)*(i*2+1-j<10)and g[i*2+1-j]or g[j]]for j in R]
#   *g,=map(list,zip(*g[::-1]))
#  return g

# def p(g):
#  for _ in[0]*4:
#   for i in range(9):
#    if{*g[i]}=={0,2}and{*g[i+1]}!={0}:
#     g=[(j<=i)*(i*2+1-j<10)and g[i*2+1-j]or g[j]for j in range(10)]
#   *g,=map(list,zip(*g[::-1]))
#  return [[v or 3 for v in s]for s in g]