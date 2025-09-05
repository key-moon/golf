def	p(g,k=range):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	k(h)]
	for	i	in	k(h):
		for	j	in	k(w):n,v=(i--2)%h,(j--3)%w;A[i][j]=g[n][v]
	return	A