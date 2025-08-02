def p(g):
	for A in g:
		if 8 in A:
			E=A.index(8);F=len(A)-1-A[::-1].index(8)
			for G in range(E,F+1):A[G]=8
	C=range(len(g))
	for D in C:
		B=[A for A in C if g[A][D]==8]
		if B:
			for H in range(B[0],B[-1]+1):g[H][D]=8
	return g