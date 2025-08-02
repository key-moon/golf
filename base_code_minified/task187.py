def p(g):
	C,D=len(g),len(g[0]);E=[(A,B)for A in(0,C-1)for B in range(D)if g[A][B]==0]+[(A,B)for A in range(1,C-1)for B in(0,D-1)if g[A][B]==0]
	while E:
		A,B=E.pop()
		if g[A][B]==0:
			g[A][B]=3
			for(F,G)in((A+1,B),(A-1,B),(A,B+1),(A,B-1)):
				if 0<=F<C and 0<=G<D and g[F][G]==0:E+=[(F,G)]
	for A in range(C):
		for B in range(D):
			if g[A][B]==0:g[A][B]=2
	return g