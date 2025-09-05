def	p(g):
	for	r	in	range(3):
		for	c	in	range(3):
			g[r][c]+=g[r][c+3]
			if	g[r][c]>0:g[r][c]=6
	g=[A[:3]for	A	in	g];return	g