def p(g):
	G=0,4,8
	for I in range(3):
		for J in range(3):
			A,B=G[I],G[J];D=None;H=set()
			for C in range(A,A+3):
				for E in range(B,B+3):
					F=g[C][E]
					if F and F!=5:D=F;H.add(C)
			if D and len(H)>1:
				for C in range(A,A+3):
					for E in range(B,B+3):g[C][E]=D
	return g