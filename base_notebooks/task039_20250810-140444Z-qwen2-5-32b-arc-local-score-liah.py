L=len
R=range
def p(g):
 h,w=L(g),L(g[0])
 P=[]
 for r in R(h):
  for c in R(w):
   if g[r][c]>0:P.append([r,c])
 a=min([i[1]for i in P])
 V=max([i[1]for i in P])
 d=min([i[0]for i in P])
 F=max([i[0]for i in P])
 V=V-((V-a)//2)
 F=F-((F-d)//2)
 g=g[d:F]
 g=[R[a:V]for R in g]
 return g