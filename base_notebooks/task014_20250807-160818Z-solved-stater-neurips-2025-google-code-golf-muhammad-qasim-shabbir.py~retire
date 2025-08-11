from collections import Counter
def p(g):
 b=[x for R in g for x in R]
 C=Counter(b).most_common(3)
 C=[c for c in C if c[0]>0][-1][0]
 g=[R for R in g if C in R]
 T=[]
 for R in g:
  for i in range(len(R)):
   if R[i]==C:T.append(i)
 g=[R[min(T):max(T)+1]for R in g]
 return g