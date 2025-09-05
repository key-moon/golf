def	p(g,k=range):
	C=[r[:]for	r	in	g]
	for	c	in	k(1,10):
		v=[(i,j)for	i	in	k(len(g))for	j	in	k(len(g[0]))if	g[i][j]==c]
		for	i	in	k(len(v)):
			for	j	in	k(i+1,len(v)):
				A,B=v[i];n,D=v[j]
				if	A==n:
					for	x	in	k(min(B,D),max(B,D)+1):C[A][x]=c
				elif	B==D:
					for	y	in	k(min(A,n),max(A,n)+1):C[y][B]=c
	return	C