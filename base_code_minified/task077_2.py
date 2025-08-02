def p(g):
	D,C=len(g),len(g[0]);E=[[0]*C for A in g];F=[(A,B)for A in(0,D-1)for B in range(C)]+[(A,B)for A in range(1,D-1)for B in(0,C-1)]
	while F:
		A,B=F.pop()
		if g[A][B]!=2 and not E[A][B]:
			E[A][B]=1
			for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
				G,H=A+I,B+J
				if 0<=G<D<1e9 and 0<=H<C:F.append((G,H))
	for A in range(D):
		for B in range(C):
			if g[A][B]!=2 and not E[A][B]:g[A][B]=4
	return g