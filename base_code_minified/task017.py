def p(A):
	B=len(A);E=[A[:]for A in A]
	for C in range(B):
		for D in range(B):
			if not E[C][D]:
				for(F,G)in((D,C),(B-1-C,D),(C,B-1-D),(B-1-C,B-1-D),(B-1-D,B-1-C),(D,B-1-C),(B-1-D,C)):
					if A[F][G]:E[C][D]=A[F][G];break
	return E