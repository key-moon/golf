def p(A):
	E,F=len(A),len(A[0]);D=[(B,C)for B in(0,E-1)for C in range(F)if A[B][C]==0]+[(B,C)for B in range(E)for C in(0,F-1)if A[B][C]==0]
	while D:
		B,C=D.pop()
		if A[B][C]==0:
			A[B][C]=-1
			if B:D+=[(B-1,C)]
			if B<E-1:D+=[(B+1,C)]
			if C:D+=[(B,C-1)]
			if C<F-1:D+=[(B,C+1)]
	for B in range(E):
		for C in range(F):
			if A[B][C]==0:A[B][C]=3
			elif A[B][C]<0:A[B][C]=0
	return A