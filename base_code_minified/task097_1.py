def p(g):
	F,G=len(g),len(g[0]);J=set();H=set()
	for A in range(F):
		for B in range(G):
			if g[A][B]and(A,B)not in J:
				I=[(A,B)];C={(A,B)}
				while I:
					M,N=I.pop()
					for K in(-1,0,1):
						for L in(-1,0,1):
							if K|L:
								D,E=M+K,N+L
								if 0<=D<F and 0<=E<G and g[D][E]and(D,E)not in C:C.add((D,E));I.append((D,E))
				J|=C
				if len(C)>len(H):H=C
	for A in range(F):
		for B in range(G):
			if g[A][B]and(A,B)not in H:g[A][B]=0
	return g