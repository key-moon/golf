def	p(g):
	A=enumerate;B=g[-1][0];g[-1][0]=0
	for(r,C)in	A(g):
		for(c,D)in	A(C):
			if	D>0:g[r][c]=B
	return	g