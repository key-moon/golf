def	p(g,u=range):
	s=[r[:]for	r	in	g]
	for	c	in	u(1,10):
		A=[(i,j)for	i	in	u(len(g))for	j	in	u(len(g[0]))if	g[i][j]==c]
		for	i	in	u(len(A)):
			for	j	in	u(i+1,len(A)):
				B,e=A[i];C,D=A[j]
				if	B==C:
					for	x	in	u(min(e,D),max(e,D)+1):s[B][x]=c
				elif	e==D:
					for	y	in	u(min(B,C),max(B,C)+1):s[y][e]=c
	return	s