def p(g):
	D,C=len(g),len(g[0]);E=[[0]*C for A in g];F=[]
	for(A,B)in[(0,A)for A in range(C)]+[(D-1,A)for A in range(C)]+[(A,0)for A in range(D)]+[(A,C-1)for A in range(D)]:
		if g[A][B]==0:E[A][B]=1;F.append((A,B))
	while F:
		G,H=F.pop()
		for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
			A,B=G+I,H+J
			if 0<=A<D and 0<=B<C and not E[A][B]and g[A][B]==0:E[A][B]=1;F.append((A,B))
	for A in range(D):
		for B in range(C):
			if g[A][B]==0 and not E[A][B]:g[A][B]=2
	return g