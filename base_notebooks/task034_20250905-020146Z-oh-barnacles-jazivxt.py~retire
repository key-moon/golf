R=range
L=len
def p(g):
 f=sum(g,[])
 C=[c for c in set(f)if c not in[0,2]][0]
 h,w=L(g),L(g[0])
 for r in R(h-1):
  for c in R(w-1):
   M=[g[r+y][c+x]for y,x in[[0,0],[0,1],[1,0],[1,1]]]
   if sum([1 for i in M if i>0])>3:
    for I in[z for z in R(L(M))if M[z]==2]:
     for i in R(10):
      if I<2:y=r-i
      else:y=r+i+1
      if I%2:x=c+i+1
      else:x=c-i
      if 0<=y<h and 0<=x<w:
       g[y][x]=C
       if 0<=y-1<h:g[y-1][x]=C
       if 0<=x-1<w:g[y][x-1]=C
       if 0<=y+1<h:g[y+1][x]=C
       if 0<=x+1<w:g[y][x+1]=C
 return g