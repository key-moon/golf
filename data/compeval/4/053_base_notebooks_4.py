def	p(g,F=range):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	F(h)]
	for	i	in	F(h):
		for	j	in	F(w):s,m=(i--2)%h,(j--3)%w;A[i][j]=g[s][m]
	return	A