def f(g,y,x,h,w):
 c=g[y][x]
 if c==0:return
 if not sum(g[y][x+i]==c for i in(1,-1))==sum(g[y+i][x]==c for i in(1,-1))==1:return
 a,b,p,q=2*(g[y+1][x]==c)-1,2*(g[y][x+1]==c)-1,x,y
 if g[y+a][x+b]==c:return
 while 1<=p<w-1 and 1<=q<h-1:q-=a;p-=b;g[q][p]=g[y+2*a][x+2*b]
def p(g):
 h,w=len(g),len(g[0])
 for y in range(1,h-1):
  for x in range(1,w-1):f(g,y,x,h,w)
 return g
