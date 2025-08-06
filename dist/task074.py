def p(g):
 for I in range(1800):
  if g[j:=I%30][i:=I//30%30]<9:g[i][j]=g[j][i]
  if i>1 and g[31-i][j]<9:g[i][j]=g[31-i][j]
 return g