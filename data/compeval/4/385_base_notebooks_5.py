def	p(g):
	h=len(g);A=enumerate
	for(r,B)in	A(g):
		for(c,C)in	A(B):
			if	r<h//2:g[r][c]=g[-(r+1)][c]
	return	g