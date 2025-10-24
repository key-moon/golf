def p(G):
 T=set();L=[]
 S={(r,c)for r,R in enumerate(G)for c,v in enumerate(R)if v}
 while S:
  Q=[S.pop()];A=0;N=[]
  while Q:
   x,y=Q.pop();v=G[x][y];N+=[(x,y,v)]
   if v==2:A=x,y
   for i in range(9):
    if(k:=(x+i//3-1,y+i%3-1))in S:S.remove(k);Q+=[k]
  a,b=A;P={(r-a,c-b,v)for r,c,v in N}
  if any(v%2 for*_,v in N):T=P
  else:L+=[(A,P)]
 E=[x for x in T if x[2]%2];C=T-{*E}
 Z=(1,-1)
 H=lambda t,r,c:([r,c][t&1]*Z[t>>1&1],[c,r][t&1]*Z[t>>2&1])
 for(a,b),U in L:
  for t in range(8):
   if{(*H(t,r,c),v)for r,c,v in C}==U:
    for r,c,v in E:
     R,K=H(t,r,c);G[R+a][K+b]=v
    break
 return G