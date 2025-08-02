def p(g):
	E=len(g);F=len(g[0]);G={}
	for K in g:
		for J in K:G[J]=G.get(J,0)+1
	C=max(G,key=G.get);D=[]
	for A in range(E):
		for B in(0,F-1):
			if g[A][B]==C:D.append((A,B))
	for B in range(F):
		for A in(0,E-1):
			if g[A][B]==C:D.append((A,B))
	while D:
		A,B=D.pop()
		if g[A][B]==C:
			g[A][B]=-1
			for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
				H,I=A+L,B+M
				if 0<=H<E and 0<=I<F and g[H][I]==C:D.append((H,I))
	for A in range(E):
		for B in range(F):
			if g[A][B]==C:g[A][B]=3
			elif g[A][B]==-1:g[A][B]=C
	return g