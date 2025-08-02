def p(g):
	D,E=len(g),len(g[0]);F=[(A,B)for A in range(D)for B in range(E)if g[A][B]<1 and A*B*(D-1-A)*(E-1-B)==0]
	while F:
		A,B=F.pop()
		if g[A][B]<1:
			g[A][B]=1
			for C in(1,-1):
				if 0<=A+C<D and g[A+C][B]<1:F.append((A+C,B))
				if 0<=B+C<E and g[A][B+C]<1:F.append((A,B+C))
	for A in range(D):
		for B in range(E):
			if g[A][B]<1:g[A][B]=2
			elif g[A][B]==1:g[A][B]=0
	return g