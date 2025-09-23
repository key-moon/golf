R=range
L=len
def p(g):
 h,w=L(g),L(g[0])
 C=g[0][w//2]
 X=[[0]*(w-1) for _ in R(h-1)]
 for r in R(h//2):
  for c in R(w//2):
   X[r][c]=g[r][c]
   X[-(r+1)][c]=g[r][c]
   X[-(r+1)][-(c+1)]=g[r][c]
   X[r][-(c+1)]=g[r][c]
 X=[[C if c>0 else 0 for c in r] for r in X]
 return X