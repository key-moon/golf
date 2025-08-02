def p(g):
	A,B=len(g),len(g[0]);I=[A for A in range(A)if g[A]==[5]*B];C=I and[0]+I+[A]or[0,A];L=[B for B in range(B)if all(g[A][B]==5 for A in range(A))];D=[0]+L+[B]
	for E in range(len(C)-1):
		for F in range(len(D)-1):
			G=C[E]+(E>0);J=C[E+1];H=D[F]+(F>0);K=D[F+1];M=g[G+(J-G)//2][H+(K-H)//2]+5
			for N in range(G,J):
				for O in range(H,K):g[N][O]=M
	return g