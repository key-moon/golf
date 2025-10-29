A=range
def p(g):
 u=sorted((r*d,i,j,r,d)for i in A(len(g))for j in A(len(g[0]))if(r:=[*g[i],2][j:].index(2))*(d:=[*[*zip(*g)][j],2][i:].index(2))if[1,*g[i]][j]if[1,*[*zip(*g)][j]][i])
 for(x,i,j,d,r)in u:
  for s in g[i:i+r]:s[j:j+d]=[(x==u[0][0])*8+(x==u[-1][0])]*d
 return g