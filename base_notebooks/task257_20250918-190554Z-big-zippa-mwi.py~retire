def p(g,L=len,R=range):
	C,D=L(g),L(g[0])
	for A in R(4):
		for B in R(4):
			if g[A][B]==0:
				if g[A][B+5]>0:g[A][B]=g[A][B+5]
			if g[A][B]==0:
				if g[A+5][B]>0:g[A][B]=g[A+5][B]
			if g[A][B]==0:
				if g[A+5][B+5]>0:g[A][B]=g[A+5][B+5]
	return[A[:4]for A in g[:4]]