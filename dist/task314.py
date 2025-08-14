def	p(g):
	u=[s[:]for	s	in	g]
	for	k	in	range(16):
		if(j:=k//2)%3<2:
			if	g[i:=k&1][j]==g[i+6][j]>1:u[i+3][j]=g[i][j]
			if	g[j][i]==g[j][i+6]>1:u[j][i+3]=g[j][i]
	return	u