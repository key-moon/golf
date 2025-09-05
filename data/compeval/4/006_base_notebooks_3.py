def	p(g):
	A=[[0,0,0],[0,0,0],[0,0,0]]
	for	r	in	range(3):
		for	c	in	range(3):
			if	g[r][c]==g[r][c+4]and	g[r][c]>0:A[r][c]=2
	return	A