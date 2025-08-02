def p(g):
	H,I=len(g),len(g[0])
	for F in range(H):
		for G in range(I):
			if not g[F][G]:
				C=[(F,G)];g[F][G]=1
				for(A,B)in C:
					for(D,E)in((A+1,B),(A-1,B),(A,B+1),(A,B-1)):
						if 0<=D<H and 0<=E<I and not g[D][E]:g[D][E]=1;C+=[(D,E)]
				J=4-len(C)
				for(A,B)in C:g[A][B]=J
	return g