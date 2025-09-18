def p(g):
 a=[(i,j)for i in range(10)for j in range(10)if g[i][j]]
 r0,r1=min(a)[0],max(a)[0]
 c0,c1=min(a,key=lambda x:x[1])[1],max(a,key=lambda x:x[1])[1]
 R=r0+r1;C=c0+c1
 for i,j in a:
  v=g[i][j];dr=2*i-R;dc=2*j-C
  for dr2,dc2 in((dc,-dr),(-dr,-dc),(-dc,dr)):
   g[(R+dr2)//2][(C+dc2)//2]=v
 return g
