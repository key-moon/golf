def p(g):
	C=[[0]*3 for A in[0]*3]
	for A in range(len(g)-1):
		for B in range(len(g[0])-1):
			if g[A][B]==2==g[A+1][B]==g[A][B+1]==g[A+1][B+1]:C[A//2][B//2]=1
	return C