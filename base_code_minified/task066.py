def p(g):
	F,G=len(g),len(g[0]);H=min(A for B in g for A in B if A not in(0,2,8));C,D=next((A,B)for A in range(F)for B in range(G)if g[A][B]==H);E=[(C,D)]
	while E:
		C,D=E.pop()
		for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
			A,B=C+I,D+J
			if 0<=A<F and 0<=B<G and g[A][B]==0:g[A][B]=H;E.append((A,B))
	return g