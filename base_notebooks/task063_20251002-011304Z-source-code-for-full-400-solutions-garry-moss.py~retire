def p(u):
 o=range;k=len(u);m=[k[:]for k in u]
 for p in range(k):
  if u[1][p]==0and u[k-2][p]==0and sum(u[k][p]for k in o(1,k-1))==0:
   for t in o(1,k-1):m[t][p]=3
 for t in range(k):
  if u[t][1]==0and u[t][k-2]==0and sum(u[t][k]for k in o(1,k-1))==0:
   for p in o(1,k-1):
    if m[t][p]==0:m[t][p]=3
 return m