def p(g):
 for c in range(10):
  z=[(i,j)for i in range(30)for j in range(30)if g[i][j]==c]
  if z and z[-1][0]-z[0][0]<5:
   y=z[0][0]+z[-1][0]>>1;x=z[0][1]+z[-1][1]>>1;g=[[max((g[k][w]==g[y][x]!=g[i][j]!=g[0][0]!=g[y+max(min(i-k,2),-2)][x+max(min(j-w,2),-2)]and g[0][0]not in g[i][min(j,w):max(j,w)]and g[0][0]not in[*zip(*g)][w][min(i,k):max(i,k)])and g[y+max(min(i-k,2),-2)][x+max(min(j-w,2),-2)]for k in range(30)for w in range(30))or g[i][j]for j in range(30)]for i in range(30)]
   for s in g[y-2:y+3]:s[x-2:x+3]=[g[0][0]]*5
   return g