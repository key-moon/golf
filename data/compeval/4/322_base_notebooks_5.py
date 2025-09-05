def	p(g):
	B=[r[:]for	r	in	g]
	for	j	in	range(len(g[0])):
		A=0
		for	i	in	range(len(g)):
			if	g[i][j]!=0:A=g[i][j]
			elif	A!=0:B[i][j]=A
	return	B