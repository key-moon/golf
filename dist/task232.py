def p(g,E=enumerate):
 for(r,D)in E(g):
  i,A,B=0,[],0
  for(c,C)in E(D):
   if C>0:A=[C,5]*20;B=1
   if B:g[r][c]=A[i];i+=1
 return g