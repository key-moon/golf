R=range
def p(g):
 c=[v for v in sum(g,[])if v][0]
 for p in R(32):
  if all((0<=p-j<16)and g[i][p-j]>0 for I in R(256)if g[i:=I%16][j:=I>>4]==c):
   return [[~(g[i][j]not in(0,c)and~g[i][p-j]or~g[i][j])for j in R(16)]for i in R(16)]
