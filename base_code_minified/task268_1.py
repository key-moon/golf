def p(g):
	D=next(A for B in g for A in B if A and A!=4);E=[(A,C)for(A,B)in enumerate(g)for(C,E)in enumerate(B)if E==D];K=min(A for(A,B)in E);L=max(A for(A,B)in E);M=min(A for(B,A)in E);N=max(A for(B,A)in E);F,G=len(g),len(g[0]);C=[A[:]for A in g]
	for A in range(M,N+1):
		if not C[K][A]:C[K][A]=D
		if not C[L][A]:C[L][A]=D
	for B in range(K,L+1):
		if not C[B][M]:C[B][M]=D
		if not C[B][N]:C[B][N]=D
	H=set();O=[(A,B)for A in(0,F-1)for B in range(G)if not C[A][B]]+[(B,A)for A in(0,G-1)for B in range(F)if not C[B][A]]
	for(B,A)in O:
		if(B,A)in H:continue
		H.add((B,A))
		for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
			I,J=B+P,A+Q
			if 0<=I<F and 0<=J<G and(I,J)not in H and not C[I][J]:O.append((I,J))
	for B in range(F):
		for A in range(G):
			if g[B][A]==0 and(B,A)not in H:g[B][A]=4
	return g