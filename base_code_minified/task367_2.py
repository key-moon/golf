def p(g):
	I=[A[:]for A in g];C,D=len(g),len(g[0]);H=[(A,B)for A in(0,C-1)for B in range(D)if g[A][B]!=5]+[(A,B)for A in range(C)for B in(0,D-1)if g[A][B]!=5];E=set()
	while H:
		A,B=H.pop()
		if(A,B)in E:continue
		E.add((A,B))
		for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
			F,G=A+J,B+K
			if 0<=F<C and 0<=G<D and g[F][G]!=5 and(F,G)not in E:H.append((F,G))
	for A in range(C):
		for B in range(D):
			if g[A][B]==0 and(A,B)not in E:I[A][B]=4
	return I