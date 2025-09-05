def	p(g,R=range,L=len):
	D=[r[:]for	r	in	g];n,m=L(g),L(g[0]);E=g[0][2]
	for	i	in	R(n):
		for	j	in	R(m):
			if	g[i][j]==E:D[i][j]=E;g[i][j]=0
			else:D[i][j]=0
	A=[r[:]for	r	in	g]
	for	c	in	R(n):
		B=[(i,j)for	i	in	R(n)for	j	in	R(m)if	g[i][j]==c]
		for	i	in	R(len(B)):
			for	j	in	R(i+1,len(B)):
				u,C=B[i];F,p=B[j]
				if	u==F:
					for	x	in	R(min(C,p),max(C,p)+1):A[u][x]=c
				elif	C==p:
					for	y	in	R(min(u,F),max(u,F)+1):A[y][C]=c
	for	i	in	R(n):
		for	j	in	R(m):
			if	D[i][j]>0:A[i][j]=E
	return	A