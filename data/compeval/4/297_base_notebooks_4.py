def	p(g):
	h,w=len(g),len(g[0]);A=g[0]*20
	for	i	in	range(2,h):g[i]=[A[i-2]for	_	in	range(w)]
	return	g