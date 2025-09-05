def	p(g):
	A=range;D=[[0]*4for	A	in	A(4)];G=[(0,0),(4,4),(4,0),(0,4)]
	for(E,F)in	G:
		for	B	in	A(4):
			for	C	in	A(4):
				if	g[E+B][F+C]:D[B][C]=g[E+B][F+C]
	return	D