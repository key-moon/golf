def p(g):
 w,h=len(g),len(g[0])
 f=lambda c:next((y,x)for y in range(w-1)for x in range(h-1)if g[y][x]==g[y+1][x+1]==c)
 y,x=f(1)
 while y>=1 and x>=1:y,x=y-1,x-1;g[y][x]=1
 y,x=f(2)
 while y<w-1 and x<h-1:y,x=y+1,x+1;g[y][x]=2
 return g