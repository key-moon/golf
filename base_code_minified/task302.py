def p(g):
	D,E=len(g),len(g[0])
	for C in range(D):
		for B in range(E):
			for A in range(3,min(D-C,E-B)+1):
				if g[C][B:B+A]==[5]*A==g[C+A-1][B:B+A]and all(g[C+D][B:B+A:A-1]==[5,5]for D in range(A)):
					for F in range(C+1,C+A-1):
						for G in range(B+1,B+A-1):g[F][G]=A+3
	return g