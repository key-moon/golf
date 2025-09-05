def	p(g):
	r,c=next((i,j)for	i	in	range(len(g))for	j	in	range(len(g[0]))if	g[i][j]==3and	all(g[i+A][j+B]==2for	A	in(-1,0,1)for	B	in(-1,0,1)if	A|B));l=[j	for	j	in	range(len(g[0]))if	g[r][j]==3and	j!=c]
	if	l:m=[j	for	j	in	l	if	j>c]or[max(l)];C,D=r,min(m)
	else:l=[i	for	i	in	range(len(g))if	g[i][c]==3and	i!=r];m=[i	for	i	in	l	if	i>r]or[max(l)];C,D=min(m),c
	for	A	in-1,0,1:
		for	B	in-1,0,1:
			if	A|B:g[r+A][c+B]=0
	for	A	in-1,0,1:
		for	B	in-1,0,1:
			if	A|B:g[C+A][D+B]=2
	return	g