C=min
B=max
A=range
def p(g):
 for c in A(10):
  z=[(i,j)for i in A(30)for j in A(30)if g[i][j]==c]
  if z and z[-1][0]-z[0][0]<5:
   y=z[0][0]+z[-1][0]>>1;x=z[0][1]+z[-1][1]>>1;g=[[B((g[k][w]==g[y][x]!=g[i][j]!=g[0][0]!=g[y+B(C(i-k,2),-2)][x+B(C(j-w,2),-2)]and g[0][0]not in g[i][C(j,w):B(j,w)]and g[0][0]not in[*zip(*g)][w][C(i,k):B(i,k)])and g[y+B(C(i-k,2),-2)][x+B(C(j-w,2),-2)]for k in A(30)for w in A(30))or g[i][j]for j in A(30)]for i in A(30)]
   for s in g[y-2:y+3]:s[x-2:x+3]=[g[0][0]]*5
   return g