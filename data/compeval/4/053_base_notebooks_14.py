def	p(g,v=range):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	v(h)]
	for	i	in	v(h):
		for	j	in	v(w):B,C=(i--2)%h,(j--3)%w;A[i][j]=g[B][C]
	return	A