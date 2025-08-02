def p(A):
	E,D=len(A),len(A[0]);F=[[0]*D for A in A];G=[]
	for B in(0,E-1):
		for C in range(D):
			if A[B][C]!=6:F[B][C]=1;G+=[(B,C)]
	for B in range(1,E-1):
		for C in(0,D-1):
			if A[B][C]!=6:F[B][C]=1;G+=[(B,C)]
	while G:
		N,O=G.pop()
		for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
			H,I=N+J,O+K
			if 0<=H<E and 0<=I<D and not F[H][I]and A[H][I]!=6:F[H][I]=1;G+=[(H,I)]
	for B in range(E):
		for C in range(D):
			if A[B][C]==8:
				if not F[B][C]:A[B][C]=4
				else:
					for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
						L,M=B+J,C+K
						if 0<=L<E and 0<=M<D and A[L][M]==6:A[B][C]=3;break
	return A