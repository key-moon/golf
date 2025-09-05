def	p(g):
	r,c=len(g),len(g[0]);t=()
	for	i	in	range(1,r-1):
		for	j	in	range(1,c-1):
			v=g[i][j]
			if	v	and	g[i-1][j]==v==g[i+1][j]and	g[i][j-1]==v==g[i][j+1]:t+=(i,j),
	for(i,j)in	t:g[i][j]=0
	return	g