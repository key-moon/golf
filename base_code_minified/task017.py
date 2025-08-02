def p(g):
	A=len(g);D=[A[:]for A in g]
	for B in range(A):
		for C in range(A):
			if not D[B][C]:
				for(E,F)in((C,B),(A-1-B,C),(B,A-1-C),(A-1-B,A-1-C),(A-1-C,A-1-B),(C,A-1-B),(A-1-C,B)):
					if g[E][F]:D[B][C]=g[E][F];break
	return D