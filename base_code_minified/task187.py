def p(A):
	D,E=len(A),len(A[0]);F=[(B,C)for B in(0,D-1)for C in range(E)if A[B][C]==0]+[(B,C)for B in range(1,D-1)for C in(0,E-1)if A[B][C]==0]
	while F:
		B,C=F.pop()
		if A[B][C]==0:
			A[B][C]=3
			for(G,H)in((B+1,C),(B-1,C),(B,C+1),(B,C-1)):
				if 0<=G<D and 0<=H<E and A[G][H]==0:F+=[(G,H)]
	for B in range(D):
		for C in range(E):
			if A[B][C]==0:A[B][C]=2
	return A