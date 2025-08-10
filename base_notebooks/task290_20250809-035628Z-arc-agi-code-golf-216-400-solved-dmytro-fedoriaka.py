m=lambda g,c,d:[[c if i==d else d for i in r]for r in g]
def p(g):
 h,w=len(g),len(g[0])
 a,b,c,d=h,0,w,0
 for y in range(h):
  for x in range(w):
   if g[y][x]:a,b,c,d=min(a,y),max(b,y),min(c,x),max(d,x)
 return m([r[c:d+1]for r in g[a:b+1]],g[a][c],g[a+(b-a)//2][c+(d-c)//2])