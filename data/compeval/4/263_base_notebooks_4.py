def	p(g):
	A=range;b=[[[g[i+r*3][j+c*3]for	j	in	A(3)]for	i	in	A(3)]for	r	in	A(len(g)//3)for	c	in	A(len(g[0])//3)]
	for	x	in	b:
		if[tuple(tuple(y[i][j]==0for	j	in	A(3))for	i	in	A(3))for	y	in	b].count(tuple(tuple(x[i][j]==0for	j	in	A(3))for	i	in	A(3)))==1:return	x