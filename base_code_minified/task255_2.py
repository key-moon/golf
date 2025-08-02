def p(g):
	D,E=len(g),len(g[0]);C=[(A,B)for A in(0,D-1)for B in range(E)if g[A][B]==0]+[(A,B)for A in range(D)for B in(0,E-1)if g[A][B]==0]
	while C:
		A,B=C.pop()
		if g[A][B]==0:
			g[A][B]=-1
			if A:C+=[(A-1,B)]
			if A<D-1:C+=[(A+1,B)]
			if B:C+=[(A,B-1)]
			if B<E-1:C+=[(A,B+1)]
	for A in range(D):
		for B in range(E):
			if g[A][B]==0:g[A][B]=3
			elif g[A][B]<0:g[A][B]=0
	return g