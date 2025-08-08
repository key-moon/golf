def p(g):
 o=0
 X=[[0 if (i+1)%4>0 and (j+1)%4>0 else 5 for i in range(11)] for j in range(11)]
 d={'00':0,'01':0,'02':0,'10':0,'11':0,'12':0,'20':0,'21':0,'22':0}
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if C>0 and C!=5:
    o=int(C)
    d[str(r//4)+str(c//4)]+=1
 m=max([d[k] for k in d])
 for r,R in E(X):
  for c,C in E(R):
   if C==0 and d[str(r//4)+str(c//4)]==m:
    X[r][c]=o
 return X
