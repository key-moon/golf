def p(d):
 G=len(d);H=len(d[0]); R=[];K=set();V={*K}
 for r in range(G):
  for c in range(H):
   if(v:=d[r][c])and(P:=(v,r,c))not in V:
    C=[P];V.add(P)
    for J in C:
     for a,b in[(0,1),(0,-1),(1,0),(-1,0)]:
      if 0<=(A:=J[1]+a)<G and 0<=(D:=J[2]+b)<H and(w:=d[A][D])and(N:=(w,A,D))not in V:V.add(N);C.append(N)
    if len(C)>3:R+=[C]
    else:K.update(C)
 for B in R:
  Z=list(zip(*B));Ro,Co=min(Z[1]),min(Z[2]);L=[(v,r-Ro,c-Co)for v,r,c in B]
  if C:=next((Ca for W in range(3,7)if(T:=9-W)and(Y:=[[(v,[W-1-c,c,T-1-r,c][i],[r,T-1-r,c,r][i])for v,r,c in L]for i in range(4)])if(C:=next((Ca for Cl in Y for A in range(-6,G)for D in range(-6,H)if(Ca:=[(v,r+A,c+D)for v,r,c in Cl])and all(0<=p[1]<G and 0<=p[2]<H for p in Ca)and sum(p in K for p in Ca)==3),0))),0):
   for v,r,c in C:d[r][c]=v
   for v,r,c in B:d[r][c]=0
 return d