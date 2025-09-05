def	p(g):
	for	c	in	range(len(g[0])):
		if	g[-1][c]==2:
			j=0
			for	i	in	range(len(g)):
				if	g[-(i+1)][c+j]==5:j+=1;g[-i][c+j]=2
				g[-(i+1)][c+j]=2
	return	g