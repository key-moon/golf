def	p(g):
	h,w=len(g),len(g[0])
	for	c	in	range(w):
		u,i=[],0
		for	r	in	range(h):u.append(g[r-h][c])
		u=[0for	x	in	u	if	x==0]+[x	for	x	in	u	if	x>0]
		for	r	in	range(h):g[r-h][c]=u[r]
	return	g