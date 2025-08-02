def p(g):
	E,F=len(g),len(g[0])
	for A in range(E):
		for B in range(F):
			if g[A][B]==3:
				for(C,D)in((1,0),(0,1),(-1,0),(0,-1)):
					if 0<=A+C<E and 0<=B+D<F and g[A+C][B+D]==2:g[A][B]=8;g[A+C][B+D]=0
	return g