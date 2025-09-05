def p(g):
 X=[]
 v=[list(r)for r in zip(*g[::-1])]
 E=[list(r)for r in zip(*v[::-1])]
 D=[list(r)for r in zip(*E[::-1])]
 for r in range(len(g)):X.append(g[r]+v[r])
 for r in range(len(g)):X.append(D[r]+E[r])
 return X