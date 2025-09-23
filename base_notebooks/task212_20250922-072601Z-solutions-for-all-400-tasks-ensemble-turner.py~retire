def p(g,L=len,R=range):
	E,F=L(g),L(g[0]);D=[A for A in R(L(g))if 5 in g[A]][0]
	for A in R(E):
		for B in R(F):
			if g[A][B]==1 and A<D:
				for C in R(A,-1,-1):g[C][B]=1
			elif g[A][B]==1 and A>D:
				for C in R(A,E):g[C][B]=1
			if g[A][B]==2 and A<D:
				for C in R(A,D):g[C][B]=2
			elif g[A][B]==2 and A>D:
				for C in R(D+1,A):g[C][B]=2
	return g
