def	p(g):
	A=range;r=[[0]*4for	_	in	A(4)];b=[(0,0),(4,4),(4,0),(0,4)]
	for(x,y)in	b:
		for	i	in	A(4):
			for	j	in	A(4):
				if	g[x+i][y+j]:r[i][j]=g[x+i][y+j]
	return	r