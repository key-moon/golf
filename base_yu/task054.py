# best: 279(jailctf merger) / others: 283(ox jam), 324(intgrah jimboko awu macaque sammyuri), 333(jacekw Potatoman nauti natte), 333(natte), 352(sekken)
def p(g):
 for c in range(10):
  z=[(i,j)for i in range(30)for j in range(30)if g[i][j]==c]
  if z and z[-1][0]-z[0][0]<5:
   y=z[0][0]+z[-1][0]>>1
   x=z[0][1]+z[-1][1]>>1
   g=[[max((g[0][0]not in g[i][min(j,w):max(j,w)] and g[0][0]not in [*zip(*g)][w][min(i,k):max(i,k)])and g[k][w]==g[y][x]!=g[i][j]!=g[0][0]!=g[y+max(min(i-k,2),-2)][x+max(min(j-w,2),-2)]and g[y+max(min(i-k,2),-2)][x+max(min(j-w,2),-2)]for k in range(30)for w in range(30)) or g[i][j] for j in range(30)]for i in range(30)]
   for s in g[y-2:y+3]:
    s[x-2:x+3]=[g[0][0]]*5
   return g

# def p(g):
#  for c in range(10):
#   z=[(i,j)for i in range(30)for j in range(30)if g[i][j]==c]
#   if len(z)>3 and z[-1][0]-z[0][0]<5:
#    y=z[0][0]+z[-1][0]>>1
#    x=z[0][1]+z[-1][1]>>1
#    for l in range(1,30):
#     for u in range(1,30):
#      r=g[u].index(g[0][0],l)
#      d=[*zip(*g)][l].index(g[0][0],u)
#      if g[0][0]==g[u-1][l]==g[u][l-1] and r-l>5:
#       g[u:d]=[[(l<=j<r)*max(g[k][w]==g[y][x]!=g[i][j]!=g[0][0]!=(v:=g[y+max(min(i-k,2),-2)][x+max(min(j-w,2),-2)])and v for k in range(u,d)for w in range(l,r)) or g[i][j] for j in range(30)]for i in range(u,d)]
#    for s in g[y-2:y+3]:
#     s[x-2:x+3]=[g[0][0]]*5
#    return g


# def p(g):
#  for c in range(10):
#   z=[(i,j)for i in range(30)for j in range(30)if g[i][j]==c]
#   if len(z)>3 and z[-1][0]-z[0][0]<5:
#    y=z[0][0]+z[-1][0]>>1
#    x=z[0][1]+z[-1][1]>>1
#    t=[]
#    for s in g[y-2:y+3]:
#     t+=s[x-2:x+3],
#     s[x-2:x+3]=[g[0][0]]*5
#    for l in range(1,30):
#     for u in range(1,30):
#      if g[u][l]!=g[0][0] and g[u-1][l]==g[u][l-1]==g[0][0]:
#       r=g[u].index(g[0][0],l)
#       d=[*zip(*g)][l].index(g[0][0],u)
#       g[u:d]=[g[i][:l]+[max(g[i][j]!=g[0][0] and g[k][w]==t[2][2] and (v:=t[2+max(min(i-k,2),-2)][2+max(min(j-w,2),-2)])!=g[0][0] and v for k in range(u,d)for w in range(l,r)) or g[i][j] for j in range(l,r)]+g[i][r:]for i in range(u,d)]
#    return g
