L=len
R=range
def p(g):
 h,w=L(g),L(g[0])
 P=[]
 for r in R(h):
  for c in R(w):
   if g[r][c]>0:P.append([r,c])
 x1=min([i[1] for i in P])
 x2=max([i[1] for i in P])
 y1=min([i[0] for i in P])
 y2=max([i[0] for i in P])
 x2=x2-((x2-x1)//2)
 y2=y2-((y2-y1)//2)
 g=g[y1:y2]
 g=[R[x1:x2] for R in g]
 return g
