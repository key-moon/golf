t=lambda g:[[g[y][x]for y in range(len(g))]for x in range(len(g[0]))]
def h(g,y,x):
 if g[y][x]!=2 or g[y][x+1]!=2:return
 for a in range(max(0,y-1),min(len(g),y+2)):
  for b in range(max(0,x-1),min(len(g[0]),x+3)):
   if g[a][b]!=2:g[a][b]=3
def f(g):
 for y in range(len(g)):
  for x in range(len(g[0])-1):h(g,y,x)
def p(g):f(g);g=t(g);f(g);return t(g)