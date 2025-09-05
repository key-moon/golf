def	p(g,L=len,R=range):
	g=g[0];C=g[0];A=L([x	for	x	in	g	if	x>0]);w=R(L(g));h=R(L(g)//2);B=[[0for	x	in	w]for	y	in	h]
	for	r	in	h:
		for	c	in	w:
			if	c<A:B[r][c]=C
		A+=1
	return	B