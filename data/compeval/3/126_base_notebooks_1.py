def	p(g):
	r=[o[:]for	o	in	g];n,m=len(g),len(g[0])
	for	i	in	range(1,n):
		for	j	in	range(1,m-1):
			if	g[i][j]==0and	g[i][j-1]and	g[i][j+1]and	g[i][j-1]==g[i][j+1]and	g[i-1][j]==g[i][j-1]:r[n-1][j]=4
	return	r