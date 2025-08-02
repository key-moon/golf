def p(g):
	C,D=len(g),len(g[0])
	for A in range(C):
		for B in range(D):
			if g[A][B]==0:g[A][B]=3
	E=[(A,B)for A in(0,C-1)for B in range(D)]+[(A,B)for A in range(C)for B in(0,D-1)]
	while E:
		A,B=E.pop()
		if g[A][B]==3:
			g[A][B]=0
			for(H,I)in((1,0),(-1,0),(0,1),(0,-1)):
				F,G=A+H,B+I
				if 0<=F<C and 0<=G<D:E.append((F,G))
	for A in range(C):
		for B in range(D):
			if g[A][B]==3:g[A][B]=2
	return g