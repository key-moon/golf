def	p(g,L=len,R=range):
	h=L(g);w=L(g[0]);A=g[h//2][:w//2];A={A[i]:A[-(i+1)]for	i	in	R(L(A))}
	for	r	in	R(h):
		for	c	in	R(w):g[r][c]=A[g[r][c]]
	return	g