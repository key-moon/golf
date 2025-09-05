L=len
R=range
def	p(g):
	B,C=[],[];h,w=L(g),L(g[0])
	for	r	in	R(h-4):
		for	c	in	R(w-4):
			A=[[g[i+r][j+c]for	i	in	R(5)]for	j	in	R(5)];A=[x	for	A	in	A	for	x	in	A];A=sum([x	for	x	in	A	if	x==1])
			if	A==16:B.append(r+2);C.append(c+2)
	for	r	in	R(h):
		for	c	in	R(w):
			if	r	in	B	or	c	in	C:
				if	g[r][c]!=1:g[r][c]=6
	return	g