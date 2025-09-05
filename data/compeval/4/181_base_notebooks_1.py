def	p(g):
	A=range;r=[x[:]for	x	in	g];b=[[g[i][j+3]for	j	in	A(3)]for	i	in	A(3)];f=[x[::-1]for	x	in	b];c=0if	g[3][3]else	6
	for	i	in	A(3):
		for	j	in	A(3):r[i][c+j]=f[i][j]
	return	r