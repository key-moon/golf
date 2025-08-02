def p(A):
	D,E=len(A),len(A[0]);F=[(0,B)for B in range(E)if A[0][B]==0]+[(D-1,B)for B in range(E)if A[D-1][B]==0]+[(B,0)for B in range(1,D-1)if A[B][0]==0]+[(B,E-1)for B in range(1,D-1)if A[B][E-1]==0]
	while F:
		B,C=F.pop()
		if A[B][C]==0:
			A[B][C]=6
			if B:F.append((B-1,C))
			if B<D-1:F.append((B+1,C))
			if C:F.append((B,C-1))
			if C<E-1:F.append((B,C+1))
	for B in range(D):
		for C in range(E):
			if A[B][C]==0:A[B][C]=4
			elif A[B][C]==6:A[B][C]=0
	return A