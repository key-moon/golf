def p(g):
	E=len(g);A=len({*sum(g,[])})-1;C=[[0]*E*A for B in range(E*A)]
	for(B,I)in enumerate(g):
		for(D,G)in enumerate(I):
			if G:
				for F in range(A):C[B*A+F][D*A:D*A+A]=[G]*A
	for H in range(E):
		for F in range(A):
			B=H*A+F
			if not C[B][B]:C[B][B]=2
			D=(E-1-H)*A+A-1-F
			if not C[B][D]:C[B][D]=2
	return C