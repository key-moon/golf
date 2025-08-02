def p(A):
	D,E=len(A),len(A[0]);F=[(B,C)for B in range(D)for C in range(E)if B*C*(D-1-B)*(E-1-C)==0 and A[B][C]==0]
	while F:
		B,C=F.pop()
		if A[B][C]==0:A[B][C]=-1;F+=(B+1,C),(B-1,C),(B,C+1),(B,C-1)
	for B in range(D):
		for C in range(E):
			if A[B][C]==0:A[B][C]=2
			elif A[B][C]<0:A[B][C]=0
	return A