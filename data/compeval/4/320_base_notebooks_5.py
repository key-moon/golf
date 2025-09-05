def	p(g,u=range):
	h,w=len(g),len(g[0]);g=[[2if	A>0else	0for	A	in	A]for	A	in	g]
	for	c	in	u(w):
		A=[g[r][c]for	r	in	u(h)][::-1];r=sum(A)//2//2
		for	i	in	u(r):g[-(i+1)][c]=8
	return	g