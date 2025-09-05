def	p(g,u=range):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	u(h)]
	for	i	in	u(h):
		for	j	in	u(w):B,C=(i--2)%h,(j--3)%w;A[i][j]=g[B][C]
	return	A