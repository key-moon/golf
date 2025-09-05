def	p(g,k=range):
	A=len(g);v=len(g[0]);n=[[0for	_	in	k(v)]for	_	in	k(A)]
	for	r	in	k(A):
		for	c	in	k(v):
			if	r==0	or	r==A-1or	c==0	or	c==v-1:n[r][c]=8
			else:n[r][c]=0
	return	n