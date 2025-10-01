def p(g):
 h,w=len(g),len(g[0])
 u=sorted((x,i,j,r,d)for I in range(h*w)if[[1]*w,*g][i:=I%h][j:=I//h]if[1,*g[i]][j]if(x:=(r:=[*g[i][j:],2].index(2))*(d:=[*[*zip(*g)][j][i:],2].index(2))))
 for x,i,j,d,r in u:
  for s in g[i:i+r]:
   s[j:j+d]=[(x==u[0][0])*8+(x==u[-1][0])]*d
 return g