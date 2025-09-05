def	p(g,k=range):
	h,w=len(g),len(g[0])
	for	c	in	k(w):
		u,i=[],0
		for	r	in	k(h):u.append(g[r-h][c])
		u=[0for	x	in	u	if	x==0]+[x	for	x	in	u	if	x>0]
		for	r	in	k(h):g[r-h][c]=u[r]
	return	g