from collections import*
def p(g):
 h,w=len(g),len(g[0])
 for r in range(0,h-3+1,1):
  for c in range(0,w-3+1,1):
   P=g[r:r+3]
   P=[R[c:c+3]for R in P]
   f=[i for s in P for i in s]
   C=Counter(f).most_common(1)
   if min(f)>0 and C[0][1]==8:return[[P[1][1]]]