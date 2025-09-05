def p(g):
 X=[]
 Q=[list(r)for r in zip(*g[::-1])]
 Y=[list(r)for r in zip(*Q[::-1])]
 R=[list(r)for r in zip(*Y[::-1])]
 for r in range(len(g)):X.append(g[r]+Q[r])
 for r in range(len(g)):X.append(R[r]+Y[r])
 return X