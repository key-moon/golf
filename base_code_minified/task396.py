def p(g):
	J,K=len(g),len(g[0]);L=0
	for Q in{B for A in g for B in A}-{0}:
		A=[(A,B)for A in range(J)for B in range(K)if g[A][B]==Q]
		if A:
			B=min(A for(A,B)in A);C=max(A for(A,B)in A);D=min(A for(B,A)in A);E=max(A for(B,A)in A);H=C-B+1;I=E-D+1
			if H>2 and I>2 and len(A)==2*(H+I)-4:
				F=H*I
				if F>L:L,F,R,S,T,U=F,F,B,C,D,E
	B,C,D,E=R,S,T,U;V=next(g[A][F]for A in range(J)for F in range(K)if g[A][F]and not(B<=A<=C and D<=F<=E));G=[g[A][D:E+1]for A in range(B,C+1)];M,N=len(G),len(G[0])
	for O in range(M):
		for P in range(N):
			if not O*(M-1)*P*(N-1):G[O][P]=V
	return G