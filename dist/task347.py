def	p(g,N=range(3)):
	for	r	in	N:
		for	c	in	N:
			g[r][c]+=g[r][c+3]
			if	g[r][c]>0:g[r][c]=6
	return[A[:3]for	A	in	g]