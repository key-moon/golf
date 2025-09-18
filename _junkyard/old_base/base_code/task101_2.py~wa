def p(g):
 m=len(g);n=len(g[0])
 P=[(i,j,v) for i,row in enumerate(g) for j,v in enumerate(row) if v]
 T=[(i,j) for i,j,v in P if v==2]
 (r1,c1),(r2,c2)=min(T),max(T)
 minh,minj=min(i for i,j,v in P),min(j for i,j,v in P)
 h=r2-r1;w=c2-c1
 dy= h//(max(i for i,j,v in P)-min(i for i,j,v in P))
 dx= w//(max(j for i,j,v in P)-min(j for i,j,v in P))
 for i,j,v in P:
  for k in range(1,dy+1):
   for l in range(1,dx+1):
    g[r1+k*(i-minh)][c1+l*(j-minj)]=v
 return g
