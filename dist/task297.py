def p(g):
 a=g[0];n=len(a)
 for i in range(len(g)-2): g[i+2]=n*[a[i%n]]
 return g