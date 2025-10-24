def n(i,r):return len(set([u[r]for u in i]))
def p(a):
 p=enumerate;o,i=len(a),len(a[0]);s=n(a,0)+n(a,-1)<len(set(a[0]))+len(set(a[-1]));a=[[r if r!=5else 0for r in r]for r in a]
 for(r,i)in p(a):
  for(u,i)in p(i):
   if s:a[r][u]=max([a[0][u],a[-1][u]])
   else:a[r][u]=max([a[r][0],a[r][-1]])
 if s:a=[[r for r in r if r>0]for r in a];a=a[:len(a[0])]
 else:a=[r for r in a if sum(r)>0];a=[r[:len(a)]for r in a]
 return a