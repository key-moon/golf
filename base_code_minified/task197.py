def p(g):
	E=next(A for A in g if 0 not in A);C=[]
	for A in E:
		if A not in C:C+=[A]
	for D in g:
		B=[]
		for A in D:
			if A and A not in B:B+=[A]
		if B and 0 in D:
			for(F,A)in enumerate(E):D[F]=B[C.index(A)]
	return g