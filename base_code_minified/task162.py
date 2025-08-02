def p(g):
	for A in range(len(g)-2):
		for B in range(len(g[0])-2):
			if not sum(sum(A[B:B+3])for A in g[A:A+3]):
				for C in g[A:A+3]:C[B:B+3]=[1]*3
				return g