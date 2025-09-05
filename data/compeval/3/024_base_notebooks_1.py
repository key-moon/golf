def	p(g):
	h,w=len(g),len(g[0]);A=[[0]*w	for	_	in	range(h)]
	for	c	in	range(w):
		if	any(g[r][c]==2for	r	in	range(h)):
			for	r	in	range(h):A[r][c]=2
	for	r	in	range(h):
		B=sorted([x	for	x	in	set(g[r])if	x	not	in[0,2]],reverse=True)
		if	B:A[r]=[B[0]]*w
	return	A