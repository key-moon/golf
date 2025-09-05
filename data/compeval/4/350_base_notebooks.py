def	p(g):
	D=[r[:]for	r	in	g]
	for	c	in	range(1,10):
		B=[(i,j)for	i	in	range(len(g))for	j	in	range(len(g[0]))if	g[i][j]==c]
		for	i	in	range(len(B)):
			for	j	in	range(i+1,len(B)):
				A,E=B[i];C,F=B[j]
				if	A==C:
					for	x	in	range(min(E,F),max(E,F)+1):D[A][x]=8
				elif	E==F:
					for	y	in	range(min(A,C),max(A,C)+1):D[y][E]=8
		for(A,C)in	B:D[A][C]=1
	return	D