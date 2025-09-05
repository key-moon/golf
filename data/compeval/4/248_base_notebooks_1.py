def	p(g):
	r=[x[:]for	x	in	g];n,m=len(g),len(g[0]);i,j,d=n-1,0,1
	while	i>=0:
		r[i][j]=1
		if	0<=j+d<m:i-=1;j+=d
		else:i-=1;d=-d;j+=d
	return	r