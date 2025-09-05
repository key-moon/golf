def	p(g):
	r,c=next((i,j)for(i,A)in	enumerate(g)for(j,x)in	enumerate(A)if	x);v=g[r][c]
	for	i	in	range(r+1):
		for	j	in	range(len(g[0])):
			if	j&1==c&1:g[i][j]=4
	g[r+1][c]=v;return	g