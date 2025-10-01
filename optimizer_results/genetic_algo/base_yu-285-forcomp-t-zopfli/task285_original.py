def	p(g):
	for	_	in	range(8):
		for	i	in	range(1,len(g)):
			for	j	in	range(1,len(g)):
				if	3<len({g[i][j],g[i-1][j],g[i][j-1],g[i-1][j-1]}):
					u=[[0]*5for	_	in	range(8)];u[0][0]=1;q=[(0,0)]
					while	q:
						(y,x),*q=q;g[i+y][j-1-x]|=g[i][j-1];g[i-1-y][j+x]|=g[i-1][j]
						for	d	in	range(9):
							if	0<y+d%3<6and	0<x+d//3<6and	1-u[y+d%3-1][x+d//3-1]and	0<g[i+y+d%3-1][j+x+d//3-1]==g[i][j]:u[y+d%3-1][x+d//3-1]=1;q+=[(y+d%3-1,x+d//3-1)]
		g[:]=map(list,zip(*g[::-1]))
	return	g