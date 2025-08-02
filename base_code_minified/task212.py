def p(g):
	E=len(g);B=next(A for(A,B)in enumerate(g)if B[0]==5)
	for(A,F)in enumerate(g):
		for(G,C)in enumerate(F):
			if 0<C<5:
				if C^1:D=range(A+1,B)if A<B else range(B+1,A)
				else:D=range(A)if A<B else range(A+1,E)
				for H in D:g[H][G]=C
	return g