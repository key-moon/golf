# p=lambda g:max([[s[l%20:[*g[l//20],0].index(0,l%20)]for s in g[l//20:[*[g[k][l%20]for k in range(20)],0].index(0,l//20)]]for l in range(400)],key=lambda t:sum(t,[]).count(2))
# p=lambda g:max([(sum(t:=[s[l%20:[*g[l//20],0].index(0,l%20)]for s in g[l//20:[*[g[k][l%20]for k in range(20)],0].index(0,l//20)]],[]).count(2),~l,t)for l in range(400)])[2]
p=lambda g:max([(sum(t:=[s[l%20:[*g[l//20],0].index(0,l%20)]for s in g[l//20:[*[*[*zip(*g)][l%20]],0].index(0,l//20)]],[]).count(2),~l,t)for l in range(400)])[2]


# def p(g):
#  V=0
#  T=[]
#  for l in range(20):
#   for u in range(20):
#    r=[*g[u],0].index(0,l)
#    d=[*[g[k][l]for k in range(20)],0].index(0,u)
#    t=[s[l:r] for s in g[u:d]]
#    v=sum(t,[]).count(2)
#    if V<v:
#     V=v
#     T=t
#  return T