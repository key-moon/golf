def	p(g):
	for	l	in	range(10):
		for	u	in	range(10):
			for	r	in	range(l,10):
				if	g[u][r]!=5:break
			for	d	in	range(u,10):
				if	g[d][l]!=5:break
			for	c	in	range(10):
				A=[i*10+j	for	i	in	range(10)for	j	in	range(10)if	g[i][j]==c];B=[i*10+j	for	i	in	range(u,d)for	j	in	range(l,r)if	g[i][j]==0]
				if[x-min(A)for	x	in	A]==[x-min(B)for	x	in	B]:
					for	x	in	A:g[x//10][x%10]=0
					for	x	in	B:g[x//10][x%10]=c
	return	g