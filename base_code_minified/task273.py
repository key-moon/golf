def p(g):
	for(E,A)in enumerate(g):
		for B in range(len(A)):
			if A[B]==4:
				for C in range(B+1,len(A)):
					if A[C]==4:
						for D in range(E+1,len(g)):
							if g[D][B]+g[D][C]==8:
								for F in range(E+1,D):
									for G in range(B+1,C):g[F][G]=2
	return g