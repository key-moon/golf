# best: 146(jailctf merger) / others: 148(xsot ovs att joking mewheni), 149(4atj sisyphus luke Seek mukundan), 157(jacekwl Potatoman nauti), 196(intgrah jimboko awu macaque sammyuri), 198(natte)
# ===================================================================== 146 ======================================================================

def p(g,x=0):
 y=g.index(max(g,key=any))
#  x=max(g).index(max(max(g),key=bool))
 while max(g)[x]<1:x+=1
 for I in range(400):
  if g[i:=I%10][j:=I//10%10]:
   g[4-j+x+y][i-y+x]|=g[i][j]
 return g

# def p(g):
#  y=g.index(max(g,key=any))
#  x=max(g).index(max(max(g),key=bool))
#  for I in range(400):
#   if g[i:=I%10][j:=I//10%10]:
#    g[4-j+x+y][i-y+x]|=g[i][j]
#  return g

# def p(g):
#  for _ in range(4):
#   y=g.index(max(g,key=any))
#   x=max(g).index(max(max(g),key=bool))
# #   y=[i for i in range(10)if any(g[i])][0]
# #   x=[i for i in range(10)if any([*zip(*g)][i])][0]
#   for i in range(10):
#    for j in range(10):
#     if g[i][j]:
#      g[4-j+x+y][i-y+x]|=g[i][j]
#   g=[*map(list,zip(*g[::-1]))]
#  return g

# def p(g):
#     H=len(g)
#     pts=[(i,j,g[i][j]) for i in range(H) for j in range(H) if g[i][j]]
#     pr=(min(i[0] for i in pts)+max(i[0] for i in pts))//2
#     pc=(min(j[1] for j in pts)+max(j[1] for j in pts))//2
#     for i,j,v in pts:
#         g[pr-(j-pc)][pc+(i-pr)]=v
#         g[2*pr-i][2*pc-j]=v
#         g[pr+(j-pc)][pc-(i-pr)]=v
#     return g



