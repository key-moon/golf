def	p(g):
	A=len(g);C=[(i,j)for	i	in	range(A)for	j	in	range(len(g[0]))if	g[i][j]==3];D=min(i	for(i,_)in	C)+.5;E=min(j	for(_,j)in	C)+.5
	for	F	in	range(A):
		for	G	in	range(len(g[0])):
			B=g[F][G]
			if	B	and	B!=3:
				J=F-D;K=G-E
				for(L,M)in(1,1),(1,-1),(-1,1),(-1,-1):
					H=int(D+L*J);I=int(E+M*K)
					if	0<=H<A	and	0<=I<len(g[0]):g[H][I]=B
	return	g