def	p(g,u=range):
	B=[r[:]for	r	in	g]
	for	c	in	u(1,10):
		A=[(i,j)for	i	in	u(len(g))for	j	in	u(len(g[0]))if	g[i][j]==c]
		for	i	in	u(len(A)):
			for	j	in	u(i+1,len(A)):
				v,b=A[i];C,D=A[j]
				if	v==C:
					for	x	in	u(min(b,D),max(b,D)+1):B[v][x]=c
				elif	b==D:
					for	y	in	u(min(v,C),max(v,C)+1):B[y][b]=c
	return	B