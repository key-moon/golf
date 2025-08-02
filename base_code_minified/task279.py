def p(A):
	E,F=len(A),len(A[0]);D=[]
	for B in range(E):
		for C in(0,F-1):
			if A[B][C]==1:D.append((B,C))
	for C in range(F):
		for B in(0,E-1):
			if A[B][C]==1:D.append((B,C))
	while D:
		B,C=D.pop()
		if A[B][C]==1:
			A[B][C]=-1
			for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
				G,H=B+I,C+J
				if 0<=G<E and 0<=H<F and A[G][H]==1:D.append((G,H))
	for B in range(E):
		for C in range(F):A[B][C]=1 if A[B][C]==-1 else 8 if A[B][C]==1 else A[B][C]
	return A