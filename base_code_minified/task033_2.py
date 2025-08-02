def p(g):
	A=g[5][0];F=[(C%6,E%6)for(C,D)in enumerate(g)for(E,B)in enumerate(D)if B and B!=A]
	for B in(0,6,12):
		for C in(0,6,12):
			for(D,E)in F:
				if g[B+D][C+E]==0:g[B+D][C+E]=A
	return g