def p(A):
	G,D=len(A),len(A[0]);H=0
	for C in range(G):
		for E in range(C,G):
			I=E-C+1;B=0;K=[all(not A[C][B]for C in range(C,E+1))for B in range(D)]
			for F in range(D+1):
				if F<D and K[F]:B+=1
				else:
					if B*I>H:H,L,M,N,J=B*I,C,E,B,F-B
					B=0
	for O in range(L,M+1):
		for P in range(J,J+N):A[O][P]=6
	return A