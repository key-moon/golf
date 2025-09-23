def p(g):
 x=0
 if g[0].count(5)==0:
  g=list(map(list,zip(*g[::-1])))
  x=3
 C=g[0].count(5)
 X=[r[:] for r in g]
 g=[[5 if c==5 else 0 for c in r] for r in g]
 s=g[0].index(5)
 for r in range(len(g)):
  M=sum([1 for c in X[r][:s] if c>0])
  N=sum([1 for c in X[r][s+C:] if c>0])
  g[r]=g[r][:s-M]+[5]*(C+M+N)+g[r][s+C+N:]
 for i in range(x):g=list(map(list,zip(*g[::-1])))
 return g