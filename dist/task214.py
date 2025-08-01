def p(g):
 b=list(zip(*[r[:3]for r in g][::-1]));c=list(zip(*b[::-1]))
 for i in 0,1,2:g[i][4:7]=b[i];g[i][8:]=c[i]
 return g