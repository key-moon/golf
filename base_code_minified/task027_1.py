def p(A):
	E,F=len(A),len(A[0])
	while 1:
		D=0
		for B in range(E):
			for C in range(F):
				if A[B][C]==0:
					if B and C and A[B-1][C]==1 and A[B][C-1]==1 and A[B-1][C-1]==1:A[B][C]=2;D=1
					elif B and C<F-1 and A[B-1][C]==1 and A[B][C+1]==1 and A[B-1][C+1]==1:A[B][C]=2;D=1
					elif B<E-1 and C and A[B+1][C]==1 and A[B][C-1]==1 and A[B+1][C-1]==1:A[B][C]=2;D=1
					elif B<E-1 and C<F-1 and A[B+1][C]==1 and A[B][C+1]==1 and A[B+1][C+1]==1:A[B][C]=2;D=1
		if not D:break
	return A