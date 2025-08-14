A=enumerate
def	p(g):
	B=g[5][0];E=[(i%6,j%6)for(i,C)in	A(g)for(j,v)in	A(C)if	v	and	v!=B]
	for	C	in	0,6,12:
		for	D	in	0,6,12:
			for(a,b)in	E:
				if	g[C+a][D+b]==0:g[C+a][D+b]=B
	return	g