def	p(g):
	r=[o[:]for	o	in	g];p=[i	for	i	in	range(10)if	g[i][9]==5];q=[j	for	j	in	range(10)if	g[0][j]==5]
	for	i	in	p:
		for	j	in	q:
			if	i>0&j<9:r[i][j]=2
	return	r