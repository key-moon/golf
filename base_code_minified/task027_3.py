def p(A):
	D,E=len(A),len(A[0]);F=[(A,B)for A in(0,D-1)for B in range(E)]+[(A,B)for A in range(D)for B in(0,E-1)]
	for(B,C)in F:
		if A[B][C]==0:A[B][C]=-1
	while F:
		B,C=F.pop()
		for(G,H)in((B-1,C),(B+1,C),(B,C-1),(B,C+1)):
			if 0<=G<D and 0<=H<E and A[G][H]==0:A[G][H]=-1;F.append((G,H))
	for B in range(D):
		for C in range(E):
			if A[B][C]==0:A[B][C]=2
			elif A[B][C]<0:A[B][C]=0
	return A