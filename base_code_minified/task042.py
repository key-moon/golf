def p(g):
	for A in range(9):
		for B in range(9):
			if g[A][B]==3:
				if g[A+1][B+1]==3:g[A+2][B-1]=8;g[A-1][B+2]=8
				if g[A+1][B-1]==3:g[A-1][B-2]=8;g[A+2][B+1]=8
	return g