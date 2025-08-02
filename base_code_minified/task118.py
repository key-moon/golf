def p(g):
	for B in g:
		C=[A for(A,B)in enumerate(B)if B==2]
		if C:
			for A in range(C[0],C[-1]+1):
				if B[A]!=2:B[A]=8
	for D in range(len(g[0])):
		E=[A for A in range(len(g))if g[A][D]==2]
		if E:
			for A in range(E[0],E[-1]+1):
				if g[A][D]!=2:g[A][D]=8
	return g