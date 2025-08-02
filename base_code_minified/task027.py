def p(A):
	E,D=len(A),len(A[0]);F=[[0]*D for A in A];G=[]
	for(B,C)in[(0,A)for A in range(D)]+[(E-1,A)for A in range(D)]+[(A,0)for A in range(E)]+[(A,D-1)for A in range(E)]:
		if A[B][C]==0:F[B][C]=1;G.append((B,C))
	while G:
		H,I=G.pop()
		for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
			B,C=H+J,I+K
			if 0<=B<E and 0<=C<D and not F[B][C]and A[B][C]==0:F[B][C]=1;G.append((B,C))
	for B in range(E):
		for C in range(D):
			if A[B][C]==0 and not F[B][C]:A[B][C]=2
	return A