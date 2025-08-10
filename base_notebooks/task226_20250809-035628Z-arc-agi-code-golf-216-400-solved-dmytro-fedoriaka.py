def f(g,y,x,c):
 if not(0<=y<len(g)and 0<=x<len(g[0])):return
 if g[y][x]:return
 g[y][x]=c
 for a,b in[(0,-1),(0,1),(-1,0),(1,0)]:f(g,y+a,x+b,c)
def p(g):
 h,w=len(g),len(g[0]);f(g,0,0,1)
 for i in range(4):f(g,h//2-1+i%2,w//2-1+i//2,2)
 f(g,h-1,w-1,3);return g