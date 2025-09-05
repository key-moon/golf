def	p(g):
	A={(i,j)for	i	in	range(len(g))for	j	in	range(len(g[0]))if	g[i][j]&2};B=3
	while	1:
		c,s,i,j=max((sum((i+~-abs(k-1)*l,j+~-abs(k-2)*l)in	A	for	k	in	range(4)for	l	in	range(k>0,s)),-s,i,j)for	s	in	range(B,5)for	i	in	range(len(g))for	j	in	range(len(g[0])));B=-s
		if	c<1:return	g
		for	k	in	range(4):
			for	l	in	range(k>0,-s):
				if(i+~-abs(k-1)*l,j+~-abs(k-2)*l)in	A:A-={(i+~-abs(k-1)*l,j+~-abs(k-2)*l)}
				elif	len(g)>i+~-abs(k-1)*l>-1<j+~-abs(k-2)*l<len(g[0]):g[i+~-abs(k-1)*l][j+~-abs(k-2)*l]=8