def	p(g):
	A=[];B=enumerate
	for(r,C)in	B(g):
		for(c,D)in	B(C):
			if	g[r][c]==1:A.append([r,c])
	for	b	in	A:
		u,j=b
		if	u>0:g[u-1][j]=2
		if	u<9:g[u+1][j]=8
		if	j>0:g[u][j-1]=7
		if	j<9:g[u][j+1]=6
	return	g