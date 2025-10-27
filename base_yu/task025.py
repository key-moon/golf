# best: 131(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 144(jailctf merger), 151(ox jam), 171(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 171(MasukenSamba), 177(import itertools)
# ============================================================== 131 ==============================================================

# p=lambda g:(0in max(g,key=sum))*[(u:=[*min(g,key=sum)],exec("for i,v in enumerate(s):\n if v in u:k=u.index(v);u[k-(i<k)+(i>k)]=v"))[0]for s in g]or[*zip(*p([*zip(*g)]))]
# p=lambda g:any(min(g))*[(u:=[*min(g,key=sum)],exec("for i,v in enumerate(s):\n if v in u:k=u.index(v);u[k-(i<k)+(i>k)]=v"))[0]for s in g]or[*zip(*p([*zip(*g)]))]
p=lambda g:[(u:=[*min(g,key=sum)],exec("for i,v in enumerate(s):\n if v in u:k=u.index(v);u[k-(i<k)+(i>k)]=v"))[0]for s in g]*any(u)or[*zip(*p([*zip(*g)]))]


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
