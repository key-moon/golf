def p(A):
	F,G=len(A),len(A[0]);D={}
	for B in range(F):
		for C in range(G):H=A[B][C];H and D.setdefault(H,[]).append((B,C))
	I=sorted(D,key=lambda I:-len(D[I]));J,E=I[0],I[1];K=[A for(A,B)in D[E]];L=[A for(B,A)in D[E]];M,N,O,P=min(K),max(K),min(L),max(L)
	for B in range(M,N+1):
		for C in range(O,P+1):
			if A[B][C]==E:A[B][C]=0
			elif A[B][C]==0 and any(0<=B+D<F and 0<=C+E<G and A[B+D][C+E]==J for(D,E)in((1,0),(-1,0),(0,1),(0,-1))):A[B][C]=J
	return A