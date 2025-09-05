def p(g,F=range):
 N=[r[:]for r in g]
 for c in F(1,10):
  s=[(i,j)for i in F(len(g))for j in F(len(g[0]))if g[i][j]==c]
  for i in F(len(s)):
   for j in F(i+1,len(s)):
    S,A=s[i]
    m,a=s[j]
    if S==m:
     for x in F(min(A,a),max(A,a)+1):N[S][x]=c
    elif A==a:
     for y in F(min(S,m),max(S,m)+1):N[y][A]=c
 return N