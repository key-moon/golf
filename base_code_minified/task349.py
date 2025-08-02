def p(A):
	E,F=len(A),len(A[0]);D=[A[:]for A in A];G=[(A,B)for A in(-1,0,1)for B in(-1,0,1)if A or B]
	for B in range(E):
		for C in range(F):
			if A[B][C]==0 and any(0<=B+D<E and 0<=C+G<F and A[B+D][C+G]==9 for(D,G)in G):D[B][C]=3
	for B in range(E):
		for C in range(F):
			if D[B][C]==0 and any(0<=B+A<E and 0<=C+G<F and D[B+A][C+G]==3 for(A,G)in G):D[B][C]=1
	return D