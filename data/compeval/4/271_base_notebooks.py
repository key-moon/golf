def	p(g,L=len,R=range):
	h,w=L(g),L(g[0]);A,z=[],0
	for	r	in	R(h-2):
		for	c	in	R(w-2):
			B=g[r][c:c+3]+g[r+1][c:c+3]+g[r+2][c:c+3];y=B.count(1)+B.count(8)/10
			if	y>z:A=B[:];z=y
	return[A[:3],A[3:6],A[6:]]