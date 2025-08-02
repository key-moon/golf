def p(g):
	A,B=next((A,B)for A in range(9)for B in range(9)if g[A][B]==g[A][B+1]==g[A+1][B]==g[A+1][B+1]==8);C=[[0]*10 for A in g]
	for D in range(10):
		for E in range(10):
			F=g[D][E]
			if F&7:C[A+(D>A)][B+(E>B)]=F
	return C