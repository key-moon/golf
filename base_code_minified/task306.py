def p(g):
	E,F=len(g),len(g[0]);K=[A for A in range(E)if g[A][0]and g[A]==[g[A][0]]*F];L=[A for A in range(F)if g[0][A]and all(g[B][A]==g[0][A]for B in range(E))];G=[-1]+K+[E];H=[-1]+L+[F];I=[(G[A]+1,G[A+1],H[B]+1,H[B+1])for A in range(len(G)-1)for B in range(len(H)-1)]
	for(A,B,C,D)in I:
		if any(g[A][B]for A in range(A,B)for B in range(C,D)):M=[A[C:D]for A in g[A:B]];N=A,B,C,D;break
	for(A,B,C,D)in I:
		if(A,B,C,D)!=N:
			for J in range(A,B):g[J][C:D]=M[J-A]
	return g