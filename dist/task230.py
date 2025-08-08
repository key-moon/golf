A=range
def p(g):
 for i in A(len(g)-1):
  for j in A(len(g[0])-1):
   if g[i][j:j+2]==[5,5]and g[i+1][j:j+2]==[5,5]:g[i-1][j-1],g[i-1][j+2],g[i+2][j-1],g[i+2][j+2]=1,2,3,4
 return g