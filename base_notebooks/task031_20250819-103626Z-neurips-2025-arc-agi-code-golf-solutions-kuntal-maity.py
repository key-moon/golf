def p(g):
 I=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 if not I:return[[]]
 R=[i for i,_ in I];C=[j for _,j in I]
 a,b=min(R),max(R);c,d=min(C),max(C)
 return[r[c:d+1]for r in g[a:b+1]]