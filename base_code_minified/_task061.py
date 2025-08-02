def p(A):
	E=len(A);F=max(map(max,A))
	for(G,D)in enumerate(A):
		for(C,H)in enumerate(D):
			if not H:
				B=G
				while not A[B][C]:B=(B+F)%E
				D[C]=A[B][C]
	return A