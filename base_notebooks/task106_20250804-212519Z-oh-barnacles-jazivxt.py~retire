def p(g):
 X=[]
 r1=[list(r) for r in zip(*g[::-1])]
 r2=[list(r) for r in zip(*r1[::-1])]
 r3=[list(r) for r in zip(*r2[::-1])]
 for r in range(len(g)):
  X.append(g[r]+r1[r])
 for r in range(len(g)):
  X.append(r3[r]+r2[r])
 return X
