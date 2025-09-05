def	p(g):
	h=len(g)
	for	c	in	range(1,len(g[0])):g[h-1][c]=4;g[h-c-1][c]=2
	return	g