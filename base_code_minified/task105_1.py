def p(g):
	for(B,C)in enumerate(g):
		for(A,D)in enumerate(C):
			if not D and 1 in C[:A]and 1 in C[A+1:]or 1 in[B[A]for B in g[:B]]and 1 in[B[A]for B in g[B+1:]]:g[B][A]=2
	return g