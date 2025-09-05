def	p(g):
	D=[r[:]for	r	in	g]
	for	c	in	range(1,10):
		A=[(i,j)for	i	in	range(len(g))for	j	in	range(len(g[0]))if	g[i][j]==c]
		for	i	in	range(len(A)):
			for	j	in	range(i+1,len(A)):
				B,C=A[i];E,F=A[j]
				if	B==E:
					for	x	in	range(min(C,F),max(C,F)+1):D[B][x]=c
				elif	C==F:
					for	y	in	range(min(B,E),max(B,E)+1):D[y][C]=c
	return	D