def	p(g):
	for	A	in	range(1800):
		if	g[j:=A%30][i:=A//30%30]<9:g[i][j]=g[j][i]
		if	i>1and	g[31-i][j]<9:g[i][j]=g[31-i][j]
	return	g