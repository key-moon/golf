def	p(g,R=range(4)):
	for	i	in	R:
		for	j	in	R:g[i][j]+=g[i+4][j]
	g=[[2if	A==0else	1for	A	in	A]for	A	in	g];g=[[0if	A!=2else	2for	A	in	A]for	A	in	g];return	g[:4]