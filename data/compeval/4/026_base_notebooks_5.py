def	p(g):
	A=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	for	r	in	range(5):
		for	c	in	range(3):
			if	g[r][c]==0and	g[r][c+4]==0:A[r][c]=8
	return	A