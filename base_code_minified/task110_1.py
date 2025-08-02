def p(A):
	F,G=len(A),len(A[0]);H=(1,0),(0,1),(-1,0),(0,-1)
	while any(0 in A for A in A):
		for B in range(F):
			for C in range(G):
				if not A[B][C]:
					for(I,J)in H:
						D,E=B+I,C+J
						if 0<=D<F and 0<=E<G and A[D][E]:A[B][C]=A[D][E];break
	return A