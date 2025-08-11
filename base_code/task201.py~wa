def p(g):
 a=sum(g,[])
 v=next(k for k in set(a) if k and a.count(k)==4)
 P=[(i,j) for i,r in enumerate(g) for j,x in enumerate(r) if x==v]
 i0,i1=min(i for i,j in P),max(i for i,j in P)
 j0,j1=min(j for i,j in P),max(j for i,j in P)
 return [r[j0:j1+1] for r in g[i0:i1+1]]
