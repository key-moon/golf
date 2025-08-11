from collections import *
L=len
R=range
def p(g):
 a=[x for R in g for x in R]
 C=Counter(a).most_common()
 C=[c for c in C if c[1]==4][0][0]
 h,w=L(g),L(g[0])
 P=[]
 for r in R(h):
  for c in R(w):
   if g[r][c]==C:P.append([r,c])
 x1=min([i[1] for i in P])
 x2=max([i[1] for i in P])
 y1=min([i[0] for i in P])
 y2=max([i[0] for i in P])
 g=g[y1+1:y2]
 g=[R[x1+1:x2] for R in g]
 h,w=L(g),L(g[0])
 for r in R(h):
  for c in R(w):
   if g[r][c]>0:g[r][c]=C
 return g
