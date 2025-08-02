def p(g):
	D,E=len(g),len(g[0]);C=[]
	for A in range(D):
		for B in(0,E-1):
			if g[A][B]==1:C.append((A,B))
	for B in range(E):
		for A in(0,D-1):
			if g[A][B]==1:C.append((A,B))
	while C:
		A,B=C.pop()
		if g[A][B]==1:
			g[A][B]=-1
			for(H,I)in((1,0),(-1,0),(0,1),(0,-1)):
				F,G=A+H,B+I
				if 0<=F<D and 0<=G<E and g[F][G]==1:C.append((F,G))
	for A in range(D):
		for B in range(E):g[A][B]=1 if g[A][B]==-1 else 8 if g[A][B]==1 else g[A][B]
	return g