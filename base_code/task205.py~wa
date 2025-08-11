def p(g):
 n,m=len(g),len(g[0]);A=0
 for i in range(n):
  for j in range(i,n):
   for k in range(m):
    for l in range(k,m):
     s=(j-i+1)*(l-k+1)
     if s<=A:continue
     S={g[x][y]for x in range(i,j+1)for y in range(k,l+1)}
     if len(S)!=2:continue
     for v in S:
      P={(x,y)for x in range(i,j+1)for y in range(k,l+1)if g[x][y]==v}
      R={x for x,y in P};T={y for x,y in P}
      if P=={(x,y)for x in R for y in range(k,l+1)}|{(x,y)for x in range(i,j+1)for y in T}:
       A=s;a,b,c,d=i,j,k,l
 return [[g[x][y]for y in range(c,d+1)]for x in range(a,b+1)]
