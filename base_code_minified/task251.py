def p(A):
	D,E=len(A),len(A[0]);F=[(B,C)for B in range(D)for C in range(E)if(B<1 or B>D-2 or C<1 or C>E-2)and not A[B][C]]
	while F:
		B,C=F.pop()
		if 0<=B<D and 0<=C<E and not A[B][C]:A[B][C]=-1;F+=[(B+1,C),(B-1,C),(B,C+1),(B,C-1)]
	for B in range(D):
		for C in range(E):
			if A[B][C]<0:A[B][C]=0
			elif not A[B][C]:A[B][C]=1
	return A