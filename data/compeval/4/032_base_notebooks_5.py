def	p(g):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	range(h)]
	for	j	in	range(w):
		B=[g[i][j]for	i	in	range(h)if	g[i][j]!=0]
		for(k,v)in	enumerate(B):A[h-len(B)+k][j]=v
	return	A