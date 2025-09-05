def	p(g):
	for	i	in	range(4):
		for	j	in	range(4):g[i][j]+=g[i+5][j]
	g=[[3if	A>0else	0for	A	in	A]for	A	in	g];g=g[:4];return	g