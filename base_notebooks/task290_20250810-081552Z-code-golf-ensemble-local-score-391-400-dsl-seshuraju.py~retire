def p(g):
 g=[R for R in g if sum(R)>0]
 T=[]
 C=[]
 for R in g:
  for i in range(len(R)):
   if R[i]>0:T.append(i);C.append(R[i])
 C=list(set(C))
 C={C[0]:C[1],C[1]:C[0]}
 g=[R[min(T):max(T)+1]for R in g]
 g=[[C[c]for c in R]for R in g]
 return g
