R=range
L=len
def p(g):
 h,w=L(g),L(g[0])
 X=[[0]*3 for _ in R(3)]
 y=min([r for r in R(h) if g[r].count(5)>0])
 x=min([r.index(5) for r in g if r.count(5)>0])
 g=[r[x:x+9] for r in g[y:y+9]]
 for r in R(0,9,3):
  for c in R(0,9,3):
   X[r//3][c//3]=g[r][c]
 g=[[X[r//3][c//3]and X[r%3][c%3]for c in R(9)]for r in R(9)]
 return g
