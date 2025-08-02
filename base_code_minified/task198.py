def p(g):
	D=max(map(max,g));J,K=(4,3)if D==9 else(3,4);I,E=len(g),len(g[0]);C=[[0]*E for A in g];F=[]
	for A in range(I):
		for B in(0,E-1):
			if g[A][B]!=D and not C[A][B]:C[A][B]=1;F.append((A,B))
	for B in range(E):
		for A in(0,I-1):
			if g[A][B]!=D and not C[A][B]:C[A][B]=1;F.append((A,B))
	while F:
		A,B=F.pop()
		for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
			G,H=A+L,B+M
			if 0<=G<I and 0<=H<E and g[G][H]!=D and not C[G][H]:C[G][H]=1;F.append((G,H))
	for A in range(I):
		for B in range(E):
			if g[A][B]!=D:g[A][B]=J if C[A][B]else K
	return g