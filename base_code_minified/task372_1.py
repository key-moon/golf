def p(g):
	A=len(g)//2
	for B in range(A):
		D,E=g[B],g[B+A+1]
		for(F,C)in enumerate(E):
			if C:D[F]=C
	g[:]=g[:A];return g