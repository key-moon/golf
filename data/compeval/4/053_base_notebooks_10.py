def	p(g):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	range(h)]
	for	i	in	range(h):
		for	j	in	range(w):B,C=(i--2)%h,(j--3)%w;A[i][j]=g[B][C]
	return	A