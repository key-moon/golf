def p(g):
	E,F=len(g),len(g[0]);G=(1,0),(0,1),(-1,0),(0,-1)
	while any(0 in A for A in g):
		for A in range(E):
			for B in range(F):
				if not g[A][B]:
					for(H,I)in G:
						C,D=A+H,B+I
						if 0<=C<E and 0<=D<F and g[C][D]:g[A][B]=g[C][D];break
	return g