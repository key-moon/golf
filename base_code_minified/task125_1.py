def p(g):
	D,C=len(g),len(g[0]);E=[[0]*C for A in g];F=[]
	for A in(0,D-1):
		for B in range(C):
			if g[A][B]!=6:E[A][B]=1;F+=[(A,B)]
	for A in range(1,D-1):
		for B in(0,C-1):
			if g[A][B]!=6:E[A][B]=1;F+=[(A,B)]
	while F:
		M,N=F.pop()
		for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
			G,H=M+I,N+J
			if 0<=G<D and 0<=H<C and not E[G][H]and g[G][H]!=6:E[G][H]=1;F+=[(G,H)]
	for A in range(D):
		for B in range(C):
			if g[A][B]==8:
				if not E[A][B]:g[A][B]=4
				else:
					for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
						K,L=A+I,B+J
						if 0<=K<D and 0<=L<C and g[K][L]==6:g[A][B]=3;break
	return g