def	p(g):
	B=[[5if	A==5else	0for	A	in	A]for	A	in	g]
	for	r	in	range(len(g)):
		for	c	in	range(len(g[r])):
			A=g[r][c]
			if	A>0and	A!=5:B[len(g)-1][c]=A
	return	B