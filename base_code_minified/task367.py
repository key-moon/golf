def p(g):
	C,D=len(g),len(g[0]);E=[(0,A)for A in range(D)if g[0][A]==0]+[(C-1,A)for A in range(D)if g[C-1][A]==0]+[(A,0)for A in range(1,C-1)if g[A][0]==0]+[(A,D-1)for A in range(1,C-1)if g[A][D-1]==0]
	while E:
		A,B=E.pop()
		if g[A][B]==0:
			g[A][B]=6
			if A:E.append((A-1,B))
			if A<C-1:E.append((A+1,B))
			if B:E.append((A,B-1))
			if B<D-1:E.append((A,B+1))
	for A in range(C):
		for B in range(D):
			if g[A][B]==0:g[A][B]=4
			elif g[A][B]==6:g[A][B]=0
	return g