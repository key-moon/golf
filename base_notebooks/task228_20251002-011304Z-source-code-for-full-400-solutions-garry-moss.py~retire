l=lambda g:[[g[t][e]for t in range(len(g))]for e in range(len(g[0]))]
def n(g):e=[g for(g,e)in enumerate(g)if any(e)];return e[0],e[-1]
def p(g):
 e,t=n(g);m,i=n(l(g))
 def r(x,n,m,t):g[x][n],g[m][t]=g[m][t],g[x][n]
 r(e+1,m+1,t+1,i+1);r(e+1,i-1,t+1,m-1);r(t-1,m+1,e-1,i+1);r(t-1,i-1,e-1,m-1);return g