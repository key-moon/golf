def p(g):a,b=g[0][:2];return[[[b,a][(i+j)&1]for j,_ in enumerate(r)]for i,r in enumerate(g)]
