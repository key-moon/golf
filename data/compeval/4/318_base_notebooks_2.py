def	p(g,R=range(4)):
	for	A	in	R:
		for	B	in	R:g[A][B]+=g[A+5][B]
	g=[[3if	A>0else	0for	A	in	A]for	A	in	g];return	g[:4]