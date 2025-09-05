def	p(g,u=range):
	C=len(g);D=len(g[0]);o=[r[:]for	r	in	g]
	for	i	in	u(C):
		A=B=None
		for	j	in	u(D):
			if	g[i][j]:
				if	A	is	not	None	and	g[i][j]==B:
					for	k	in	u(A+1,j):o[i][k]=B
				A=j;B=g[i][j]
	for	j	in	u(D):
		A=B=None
		for	i	in	u(C):
			if	g[i][j]:
				if	A	is	not	None	and	g[i][j]==B:
					for	k	in	u(A+1,i):o[k][j]=B
				A=i;B=g[i][j]
	return	o