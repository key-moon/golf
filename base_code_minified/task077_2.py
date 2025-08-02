def p(A):
	E,D=len(A),len(A[0]);F=[[0]*D for A in A];G=[(A,B)for A in(0,E-1)for B in range(D)]+[(A,B)for A in range(1,E-1)for B in(0,D-1)]
	while G:
		B,C=G.pop()
		if A[B][C]!=2 and not F[B][C]:
			F[B][C]=1
			for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
				H,I=B+J,C+K
				if 0<=H<E<1e9 and 0<=I<D:G.append((H,I))
	for B in range(E):
		for C in range(D):
			if A[B][C]!=2 and not F[B][C]:A[B][C]=4
	return A