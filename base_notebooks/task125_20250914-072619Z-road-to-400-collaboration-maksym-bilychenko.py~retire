R=range
L=len
def p(g):
 g=[[8]+r+[8] for r in g]
 g=[[8]*len(g[0])]+g+[[8]*len(g[0])]
 h,w=L(g),L(g[0])
 S=[-1,0,1]
 S=[[x,y] for x in S for y in S]
 for r in R(1,h-1):
  for c in R(1,w-1):
   if g[r][c]==8:
    M=[g[r+y][c+x] for y,x in S]
    if M.count(6)+M.count(4)>3:g[r][c]=4
 for r in R(1,h-1):
  for c in R(1,w-1):
   M=[g[r+y][c+x] for y,x in S]
   if g[r][c]==8 and M.count(6)>0:g[r][c]=3
 g=[r[1:-1] for r in g[1:-1]]
 return g