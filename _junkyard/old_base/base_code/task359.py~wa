def p(g):
 r=[max(set(x),key=x.count)for x in g]
 c=[max(set(x),key=x.count)for x in zip(*g)]
 return [c]*len(g)if len(set(c))<len(set(r))else[[r[i]]*len(g[0])for i in range(len(g))]
