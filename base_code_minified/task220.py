def p(g,m={2:1,3:6,8:4}):
	E,F=len(g),len(g[0])
	for A in range(E):
		for B in range(F):
			G=g[A][B]
			if G:
				H=m[G]
				for C in(-1,0,1):
					for D in(-1,0,1):
						if C|D and 0<=A+C<E and 0<=B+D<F:g[A+C][B+D]=H
	return g