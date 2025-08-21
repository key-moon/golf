def p(g):
 m=[0,1,2,3,4,5,6,7,8,9]
 t=[r[::-1]for r in g]
 x=t
 I=[(i,j)for i,r in enumerate(x)for j,v in enumerate(r)if v]
 if not I:return[[]]
 R=[i for i,_ in I];C=[j for _,j in I]
 a,b=min(R),max(R);c,d=min(C),max(C)
 x=[r[c:d+1]for r in x[a:b+1]]
 return[[m[v]for v in r]for r in x]