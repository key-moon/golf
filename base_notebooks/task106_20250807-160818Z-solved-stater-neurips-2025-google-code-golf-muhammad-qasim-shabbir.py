def p(g):
 X=[]
 j=[list(r)for r in zip(*g[::-1])]
 b=[list(r)for r in zip(*j[::-1])]
 u=[list(r)for r in zip(*b[::-1])]
 for r in range(len(g)):X.append(g[r]+j[r])
 for r in range(len(g)):X.append(u[r]+b[r])
 return X