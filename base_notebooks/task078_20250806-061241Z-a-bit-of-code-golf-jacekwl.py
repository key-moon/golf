def p(g,s=range):
 h,w=len(g),len(g[0])
 y=[[0]*w for _ in s(h)]
 for j in s(w):
  O=[g[i][j]for i in s(h)if g[i][j]!=0]
  for k,v in enumerate(O):y[k][j]=v
 return y