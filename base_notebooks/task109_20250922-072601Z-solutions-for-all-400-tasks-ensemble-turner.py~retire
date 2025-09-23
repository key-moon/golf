R=range;L=len
def p(g):
 h,w=L(g),L(g[0]);C=g[0][w//2];X=[[0]*(w-1)for _ in R(h-1)]
 for r in R(h//2):
  s=~r
  for c in R(w//2):
   t=~c;v=C*(g[r][c]>0)
   X[r][c]=X[s][c]=X[s][t]=X[r][t]=v
 return X