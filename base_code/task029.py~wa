def p(g):
 a,b=[i for i,x in enumerate(g)
      if any(all(x[j]==x[j+k]for k in range(4))
             for j in range(len(x)-3))]
 x=g[a]
 j=next(j for j in range(len(x)-3)
        if all(x[j]==x[j+k]for k in range(4)))
 k=j+x[j:].count(x[j])
 return [r[j+1:k] for r in g[a+1:b]]
