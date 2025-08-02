def p(g):
	D,E=len(g),len(g[0]);C=[A[:]for A in g];F=[(A,B)for A in(-1,0,1)for B in(-1,0,1)if A or B]
	for A in range(D):
		for B in range(E):
			if g[A][B]==0 and any(0<=A+C<D and 0<=B+F<E and g[A+C][B+F]==9 for(C,F)in F):C[A][B]=3
	for A in range(D):
		for B in range(E):
			if C[A][B]==0 and any(0<=A+F<D and 0<=B+G<E and C[A+F][B+G]==3 for(F,G)in F):C[A][B]=1
	return C