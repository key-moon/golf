def	p(g):
	*_,B,A,C=sorted({*sum(g,[])},key=sum(g,[]).count)
	for	_	in	range(4):
		if	len(g)>len(g[0])and	A	in	g[0]:
			for	c	in	range(4,0,-1):
				for	u	in	range(len(g)//2):
					for	l	in	range(len(g[0])):
						for	y	in	range(len(g)//2-u,0,-1):
							for	x	in	range(len(g[0])-l,0,-1):
								if	sum(B!=g[u+i][j+l]for	i	in	range(y)for	j	in	range(x))==c*all(A!=g[u+i][j+l]for	i	in	range(y)for	j	in	range(x)):
									for	n	in	range(len(g)//2-y+1):
										for	m	in	range(len(g[0])-x+1):
											if	all([C,g[u+i][j+l]][B!=g[u+i][j+l]]==g[len(g)//2+n+i][j+m]for	i	in	range(y)for	j	in	range(x)):
												for	i	in	range(y):
													for	j	in	range(x):g[len(g)//2+n+i][j+m]=g[u+i][j+l]
									for	i	in	range(y):
										for	j	in	range(x):g[u+i][j+l]=A
			g=g[len(g)//2:]
		g=[*map(list,zip(*g[::-1]))]
	return	g