def p(A):
	D,E=len(A),len(A[0])
	for B in range(D):
		for C in range(E):
			if A[B][C]==0:A[B][C]=3
	F=[(A,B)for A in(0,D-1)for B in range(E)]+[(A,B)for A in range(D)for B in(0,E-1)]
	while F:
		B,C=F.pop()
		if A[B][C]==3:
			A[B][C]=0
			for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
				G,H=B+I,C+J
				if 0<=G<D and 0<=H<E:F.append((G,H))
	for B in range(D):
		for C in range(E):
			if A[B][C]==3:A[B][C]=2
	return A