def	p(g):
	for	r	in	range(4):
		for	c	in	range(3):
			g[r][c]+=g[r][c+4]
			if	g[r][c]>0:g[r][c]=0
			else:g[r][c]=3
	return[A[:3]for	A	in	g]