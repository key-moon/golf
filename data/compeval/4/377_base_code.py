def p(g):
 d=lambda a:[a[0]]+[a[i] for i in range(1,len(a)) if a[i]!=a[i-1]]
 g=d(g)
 g=[list(x) for x in zip(*d(list(zip(*g))))]
 return g
