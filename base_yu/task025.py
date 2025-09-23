# best: 131(4atj sisyphus luke Seek mukundan) / others: 151(ox jam), 163(jailctf merger), 177(2F), 177(biz), 187(natte)
# ============================================================== 131 ==============================================================

p=lambda g:(0in max(g,key=sum))*[(u:=[*min(g,key=sum)],exec("for i,v in enumerate(s):\n if v in u:k=u.index(v);u[k-(i<k)+(i>k)]=v"))[0]for s in g]or[*zip(*p([*zip(*g)]))]

# def p(g):
#  t=[]
#  for s in g:
#   t+=[u:=[*min(g,key=sum)]]
#   for i,v in enumerate(s):
#    if v in u:
#     k=u.index(v)
#     u[k-(i<k)+(i>k)]=v
#  return (0in max(g,key=sum))*t or[*zip(*p([*zip(*g)]))]


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
