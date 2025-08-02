def p(g):
	for(F,C)in enumerate(g):
		if 3 in C:G=C.index(3);break
	H=F+1;I=G+1
	for(E,C)in enumerate(g):
		for(A,D)in enumerate(C):
			if D and D-3:
				if F<=E<=H:
					if A<G:
						for B in range(A,G):C[B]=D
					elif A>I:
						for B in range(I+1,A+1):C[B]=D
				elif G<=A<=I:
					if E<F:
						for B in range(E,F):g[B][A]=D
					elif E>H:
						for B in range(H+1,E+1):g[B][A]=D
	return g