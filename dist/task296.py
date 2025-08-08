A=range
def p(g):
 o=[[0]*3for _ in[0]*3]
 for i in A(5):
  for j in A(7):
   if g[i][j]:o[i-(i>1)*2][j-(j>2)*4]=g[i][j]
 return o