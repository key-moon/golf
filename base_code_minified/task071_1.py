def p(g):
	E,F=len(g),len(g[0]);C={}
	for A in range(E):
		for B in range(F):G=g[A][B];G and C.setdefault(G,[]).append((A,B))
	H=sorted(C,key=lambda k:-len(C[k]));I,D=H[0],H[1];J=[A for(A,B)in C[D]];K=[A for(B,A)in C[D]];L,M,N,O=min(J),max(J),min(K),max(K)
	for A in range(L,M+1):
		for B in range(N,O+1):
			if g[A][B]==D:g[A][B]=0
			elif g[A][B]==0 and any(0<=A+C<E and 0<=B+D<F and g[A+C][B+D]==I for(C,D)in((1,0),(-1,0),(0,1),(0,-1))):g[A][B]=I
	return g