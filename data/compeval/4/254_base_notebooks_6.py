def	p(g,R=range):
	E,D=len(g),len(g[0]);B=[0for	A	in	R(D)]
	for	A	in	R(D):
		for	C	in	R(E):
			if	g[C][A]>0:B[A]+=1
			g[C][A]=0
	F=min([A	for	A	in	B	if	A>0]);A=B.index(F)
	for	C	in	R(B[A]):g[-(C+1)][A]=2
	A=B.index(max(B))
	for	C	in	R(B[A]):g[-(C+1)][A]=1
	return	g