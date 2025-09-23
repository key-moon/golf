L=len
R=range
P=[[0,0],[0,1],[1,0],[1,1]]
def p(g):
 h,w=L(g),L(g[0])
 C=[c for c in set(sum(g,[])) if c not in [0,5]][0]
 for r in R(h-1):
  for c in R(w-1):
    M=[g[r+y][c+x] for y,x in P]
    if M.count(5)==1 and sum(M)==5:
     for y in R(2):
      for x in R(2):
        if g[y+r][x+c]==5:
          for z in R(-10,10):
           if M[2]==5:
            if 0<=y+r-z-1<h and 0<=x+c-z+1<w:g[y+r-z-1][x+c-z+1]=C
           else:
            if 0<=y+r-z+1<h and 0<=x+c-z-1<w:g[y+r-z+1][x+c-z-1]=C
 g=[[c if c!=5 else 0 for c in r] for r in g]
 return g