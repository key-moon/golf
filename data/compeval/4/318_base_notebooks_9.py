def	p(g,R=range(4)):
	for	i	in	R:
		for	j	in	R:g[i][j]+=g[i+5][j]
	g=[[3if	A>0else	0for	A	in	A]for	A	in	g];return	g[:4]