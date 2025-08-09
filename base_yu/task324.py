def p(g):
 G=sum(g,[])
 c=sorted((G.count(v),v)for v in{*G})
 m={}
 a=set()
 b=set()
 k=0
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]in(c[0][1],c[1][1]):
    f,*r={g[k][j]for k in range(len(g))if k!=i}-{g[i][j]}
    F,*R={g[i][k]for k in range(len(g[0]))if k!=j}-{g[i][j]}
    if r and R:
     k=g[i][j]
    else:
     m[g[i][j]]=m[u:=[F,f][not r]]=g[i][j]
    a|={i-j}
    b|={i+j}
 if k:m[k]=m[c[2][1]^c[3][1]^u]=k
 for i in range(len(g)):
  for j in range(len(g[0])):
   if i-j in a or i+j in b:
    g[i][j]=m[g[i][j]]
 return g
