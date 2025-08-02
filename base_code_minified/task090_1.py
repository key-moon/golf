def p(A):
	F,G=len(A),len(A[0]);H=0;I=J=K=L=0
	for B in range(F):
		for D in range(B+1,F+1):
			for C in range(G):
				for E in range(C+1,G+1):
					if(D-B)*(E-C)>H and all(not A[B][D]for B in range(B,D)for D in range(C,E)):H=(D-B)*(E-C);I=B;J=D;K=C;L=E
	for M in range(I,J):
		for N in range(K,L):A[M][N]=6
	return A