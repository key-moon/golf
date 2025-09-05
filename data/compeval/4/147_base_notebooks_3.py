def	p(j):
	B=[k[:]for	k	in	j];c,C=len(j),len(j[0])
	for	k	in	range(c):
		for	A	in	range(C):
			if	j[k][A]==3:
				for(l,D)in[(0,1),(1,0),(0,-1),(-1,0)]:
					if	0<=k+l<c	and	0<=A+D<C	and	j[k+l][A+D]==3:B[k][A]=8;break
	return	B