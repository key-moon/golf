def p(g):
 d={};m=0
 for i,r in enumerate(g):
  j=0
  while j<len(r):
   k=j+1
   while k<len(r)and r[k]==r[j]:k+=1
   if k-j>1:d.setdefault((j,k),[]).append(i)
   j=k
 for(j,k),rs in d.items():
  if len(rs)==2 and k-j>m:
   m,k0,j0,A,B=k-j,k,j,*sorted(rs)
 return [row[j0+1:k0-1]for row in g[A+1:B]]
