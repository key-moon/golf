def	p(g):
	for	i	in	range(4):
		for	j	in	range(4):g[i][j]+=g[i+4][j]
	g=[[2if	A==0else	1for	A	in	A]for	A	in	g];g=[[0if	A!=2else	2for	A	in	A]for	A	in	g];g=g[:4];return	g