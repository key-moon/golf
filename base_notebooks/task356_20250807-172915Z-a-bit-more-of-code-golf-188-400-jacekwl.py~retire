def p(g,R=range):
 E=[r[:]for r in g]
 for c in R(1,10):
  C=[(i,j)for i in R(len(g))for j in R(len(g[0]))if g[i][j]==c]
  for i in R(len(C)):
   for j in R(i+1,len(C)):
    v,D=C[i];V,a=C[j]
    if v==V:
     for x in R(min(D,a),max(D,a)+1):E[v][x]=c
    elif D==a:
     for y in R(min(v,V),max(v,V)+1):E[y][D]=c
 return E