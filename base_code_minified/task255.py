def p(g):
	B=0;J,E=len(g),len(g[0]);F=[0]*E
	for C in range(J):
		G=[0]*E
		for A in range(E):
			if not g[C][A]:
				D=1
				if C*A:D=min(F[A],F[A-1],G[A-1])+1
				G[A]=D
				if D>B:B,H,I=D,C,A
		F=G
	for C in range(H-B+1,H+1):g[C][I-B+1:I+1]=[3]*B
	return g