def	p(g):
	for	i	in	range(9):
		for	j	in	range(9):
			if	g[i][j]==5:
				for	A	in-1,0,1:
					for	B	in-1,0,1:
						try:g[i+A][j+B]=g[i+A][j+B]or	1
						except:pass
	return	g