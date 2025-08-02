def p(A):
	D,E=len(A),len(A[0])
	for B in range(D):
		for C in range(E):
			if A[B][C]==3 and(B and A[B-1][C]==3 or B<D-1 and A[B+1][C]==3 or C and A[B][C-1]==3 or C<E-1 and A[B][C+1]==3):A[B][C]=8
	return A