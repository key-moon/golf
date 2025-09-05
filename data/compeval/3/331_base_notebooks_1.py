def	p(g,E=enumerate):
	A=[]
	for(r,B)in	E(g):
		for(c,C)in	E(B):
			if	g[r][c]==1:A+=[[r,c]]
	for	v	in	A:
		a,i=v
		if	a>0:g[a-1][i]=2
		if	a<9:g[a+1][i]=8
		if	i>0:g[a][i-1]=7
		if	i<9:g[a][i+1]=6
	return	g