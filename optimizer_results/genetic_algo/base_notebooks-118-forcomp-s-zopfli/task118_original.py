B=range
A=len
def p(p):
 t={(l,n)for l in B(A(p))for n in B(A(p[0]))if p[l][n]&2};d=lambda i,l:[i and(d(i[1:],l)or not i[0]&l and d(i[1:],l|i[0])),l][t<=l]
 for n in 2,3:
  l=[l for d in B(A(p))for i in B(A(p[0]))for l in[{(l,n)for l in B(-n,n+1)for(l,n)in[(d+l,i),(d,i+l)]if A(p)>l>-1<n<A(p[0])}]if min(p[l][n]for(l,n)in l)&2]
  if l:=d(l,set()):
   for(l,n)in l:p[l][n]+=3*(p[l][n]&1)
   return p