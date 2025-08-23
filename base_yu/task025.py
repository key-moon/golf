def p(g):
 if~-any(all(s)for s in g):
  t=[]
  for s in g:
   t+=[u:=[x&y for x,y in zip(g[0],g[1])]]
   for i,v in enumerate(s):
    if v in u:
     k=u.index(v)
     u[k-(i<k)+(i>k)]=v
  return t
 return[*zip(*p([*zip(*g)]))]


# def p(g):
#  for _ in 0,1:
#   if~-any(all(s)for s in g):
#    t=[]
#    for s in g:
#     t+=[u:=[x&y for x,y in zip(g[0],g[1])]]
#     for i,v in enumerate(s):
#      if v in u:
#       k=u.index(v)
#       u[k-(i<k)+(i>k)]=v
#    g=t
#   *g,=map(list,zip(*g))
#  return g
