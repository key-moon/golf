def p(m):
 n=len(m);c=[sum(r[j]==5for r in m)for j in range(n)]
 s=sorted({v for v in c if v},reverse=1)
 M={v:i+1for i,v in enumerate(s)}
 o=[r[:]for r in m]
 for i in range(n):
  for j in range(n):
   if o[i][j]==5:o[i][j]=M.get(c[j],0)
 return o
