def p(g):
	C,D=len(g),len(g[0]);E=[(A,B)for A in(0,C-1)for B in range(D)]+[(A,B)for A in range(C)for B in(0,D-1)]
	for(A,B)in E:
		if g[A][B]==0:g[A][B]=-1
	while E:
		A,B=E.pop()
		for(F,G)in((A-1,B),(A+1,B),(A,B-1),(A,B+1)):
			if 0<=F<C and 0<=G<D and g[F][G]==0:g[F][G]=-1;E.append((F,G))
	for A in range(C):
		for B in range(D):
			if g[A][B]==0:g[A][B]=2
			elif g[A][B]<0:g[A][B]=0
	return g