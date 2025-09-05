def	p(g,E=range):
	h,w=len(g),len(g[0]);g=[[2if	A>0else	0for	A	in	A]for	A	in	g]
	for	c	in	E(w):
		A=[g[r][c]for	r	in	E(h)][::-1];r=sum(A)//2//2
		for	i	in	E(r):g[-(i+1)][c]=8
	return	g