def p(A):
	E,F=len(A),len(A[0]);G=[(B,C)for B in range(E)for C in range(F)if A[B][C]<1 and B*C*(E-1-B)*(F-1-C)==0]
	while G:
		B,C=G.pop()
		if A[B][C]<1:
			A[B][C]=1
			for D in(1,-1):
				if 0<=B+D<E and A[B+D][C]<1:G.append((B+D,C))
				if 0<=C+D<F and A[B][C+D]<1:G.append((B,C+D))
	for B in range(E):
		for C in range(F):
			if A[B][C]<1:A[B][C]=2
			elif A[B][C]==1:A[B][C]=0
	return A