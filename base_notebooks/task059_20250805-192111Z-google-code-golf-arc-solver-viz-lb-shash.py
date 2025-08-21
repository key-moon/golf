def p(g,E=enumerate,N=range(11)):
 o=0;X=[[0 if(i+1)%4>0and(j+1)%4>0 else 5 for i in N]for j in N];d={'00':0,'01':0,'02':0,'10':0,'11':0,'12':0,'20':0,'21':0,'22':0}
 for r,R in E(g):
  for c,C in E(R):
   if C>0and C!=5:o=int(C);d[str(r//4)+str(c//4)]+=1
 m=max(d.values())
 for r,R in E(X):
  for c,C in E(R):
   if C==0and d[str(r//4)+str(c//4)]==m:X[r][c]=o
 return X