def	p(g):
	n=len(g)-1
	for	i	in	range(n):
		for	j	in	range(n):
			if	g[i][j]+g[i][j+1]+g[i+1][j]+g[i+1][j+1]==24:
				if	not	g[i][j]:g[i][j]=1
				elif	not	g[i][j+1]:g[i][j+1]=1
				elif	not	g[i+1][j]:g[i+1][j]=1
				else:g[i+1][j+1]=1
	return	g