def p(g,Q=range):
 G=len(g);K=lambda g:[*map(list,zip(*g[::-1]))]
 for O in Q(4):
  l=[(A,T)for A in Q(G)for T in Q(G)if g[A][T]];L,M=zip(*l);T,H,D,e=min(L),max(L),min(M),max(M);N=g[T][D];o=g[T].count(N)
  if o<g[H].count(N):
   l,a=D+o//2,e-o//2
   for A in Q(H):g[A][l:a+1]=[4]*(a-l+1)
   for A in Q(T+1,H):g[A][D+1:e]=[4]*(e-D-1)
   for C in Q(T+1):
    A=T-C
    if l>=C:g[A][l-C]=4
    if a+C<G:g[A][a+C]=4
   for A in Q(4-O):g=K(g)
   return g
  g=K(g)