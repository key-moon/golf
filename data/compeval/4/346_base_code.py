def	p(g):
	for	i	in	range(len(g)-2):
		for	j	in	range(len(g[0])-2):
			v=g[i][j];c=g[i+1][j+1]
			if	v	and	c!=v	and	all(g[i+u][j+w]==v	for(u,w)in((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2))):return[[c]]