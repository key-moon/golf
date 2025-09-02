t=lambda g:[[g[y][x]for y in range(len(g))]for x in range(len(g[0]))]
def b(g):a=[i for i,r in enumerate(g)if any(r)];return a[0],a[-1]
def p(g):
 y,q=b(g)
 x,p=b(t(g))
 def s(a,b,c,d):g[a][b],g[c][d]=g[c][d],g[a][b]
 s(y+1,x+1,q+1,p+1)
 s(y+1,p-1,q+1,x-1)
 s(q-1,x+1,y-1,p+1)
 s(q-1,p-1,y-1,x-1)
 return g
