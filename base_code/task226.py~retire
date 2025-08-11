def p(g):
 h=len(g);w=len(g[0])
 y=[i for i,r in enumerate(g) if r.count(5)==w]
 x=[j for j in range(w) if all(g[i][j]==5 for i in range(h))]
 Y=[-1]+y+[h];X=[-1]+x+[w]
 b=[(Y[i]+1,Y[i+1]-1) for i in range(len(Y)-1) if Y[i]+1<Y[i+1]]
 c=[(X[i]+1,X[i+1]-1) for i in range(len(X)-1) if X[i]+1<X[i+1]]
 R=len(b);S=len(c)
 for k in range(3):
  v=k+1;I=(0,(R-1)//2,R-1)[k];J=(0,(S-1)//2,S-1)[k];a,A=b[I];C,D=c[J]
  for r in range(a,A+1):
   for j in range(C,D+1):g[r][j]=v
 return g
