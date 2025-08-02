def p(g):
	D,E=len(g),len(g[0]);A=[A[:]for A in g]
	for B in range(D):
		for C in range(E):
			if A[B][C]==0:A[B][C]=2
	F=[(0,A)for A in range(E)]+[(D-1,A)for A in range(E)]+[(A,0)for A in range(D)]+[(A,E-1)for A in range(D)]
	while F:
		B,C=F.pop()
		if A[B][C]==2:
			A[B][C]=0
			for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
				G,H=B+I,C+J
				if 0<=G<D and 0<=H<E and A[G][H]==2:F.append((G,H))
	return A