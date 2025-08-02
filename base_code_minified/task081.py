def p(g):
	C=len(g)-1
	for A in range(C):
		for B in range(C):
			if g[A][B]+g[A][B+1]+g[A+1][B]+g[A+1][B+1]==24:
				if not g[A][B]:g[A][B]=1
				elif not g[A][B+1]:g[A][B+1]=1
				elif not g[A+1][B]:g[A+1][B]=1
				else:g[A+1][B+1]=1
	return g