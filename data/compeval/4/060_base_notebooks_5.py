def	p(g):
	w=len(g[0]);h=int((w-1)/2);A=enumerate
	for(r,B)in	A(g):
		if	max(B)>0:
			for	x	in	range(h):g[r][x]=g[r][0];g[r][w-x-1]=g[r][w-1]
			g[r][h]=5
	return	g