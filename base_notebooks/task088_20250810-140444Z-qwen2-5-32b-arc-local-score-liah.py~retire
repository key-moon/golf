from collections import*
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
 F=min([i[1]for i in P])
 V=max([i[1]for i in P])
 d=min([i[0]for i in P])
 k=max([i[0]for i in P])
 g=g[d+1:k]
 g=[R[F+1:V]for R in g]
 h,w=L(g),L(g[0])
 for r in R(h):
  for c in R(w):
   if g[r][c]>0:g[r][c]=C
 return g