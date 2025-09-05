def	p(g):
	A={3:6,8:4,2:1}
	for(E,F)in	enumerate(g):
		for(G,B)in	enumerate(F):
			if	B	in	A:
				for	C	in-1,0,1:
					for	D	in-1,0,1:
						if	C	or	D:g[E+C][G+D]=A[B]
	return	g