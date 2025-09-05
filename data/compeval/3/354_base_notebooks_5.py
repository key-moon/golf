def	p(g):
	A=range;r=[x[:]for	x	in	g]
	def	d(i,j,c):
		if	0<=i<10and	0<=j<10and	r[i][j]==5:r[i][j]=c;[d(i+a,j+b,c)for(a,b)in[(-1,0),(1,0),(0,-1),(0,1)]]
	[[d(i,j,g[0][j])for	i	in	A(1,10)if	r[i][j]==5]for	j	in	A(10)if	g[0][j]];return	r