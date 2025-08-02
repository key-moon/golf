def p(A):
	F,G=len(A),len(A[0])
	for B in range(F):
		for C in range(G):
			if A[B][C]and(B*C<1 or not A[B-1][C-1]):
				H=0;D=B;E=C
				while D<F and E<G and A[D][E]:
					if H&1:A[D][E]=4
					H+=1;D+=1;E+=1
	return A