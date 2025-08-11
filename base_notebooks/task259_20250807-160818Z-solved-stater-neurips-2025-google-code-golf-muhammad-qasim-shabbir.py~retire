def p(g):
 for r in range(len(g)):
  for c in range(len(g[0])):
   if g[r][c]==1:g[r][c]=0
 T=[]
 for i in range(len(g)):
  if sum(g[i])>0:T.append(i)
 g=g[min(T):max(T)+1]
 T=[]
 for R in g:
  for i in range(len(R)):
   if R[i]>0:T.append(i)
 g=[R[min(T):max(T)+1] for R in g]
 return g
