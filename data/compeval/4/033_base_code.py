def	p(g):
	A=g[5][0];D=[(i%6,j%6)for(i,B)in	enumerate(g)for(j,v)in	enumerate(B)if	v	and	v!=A]
	for	B	in	0,6,12:
		for	C	in	0,6,12:
			for(a,b)in	D:
				if	g[B+a][C+b]==0:g[B+a][C+b]=A
	return	g