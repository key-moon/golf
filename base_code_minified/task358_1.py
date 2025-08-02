def p(g):
	A=len(g);E=len(g[0]);C=max(range(A),key=lambda i:sum(map(bool,g[i])));D=[A for A in g[C]if A];H=g[C].index(D[0]);B=max(range(E),key=lambda j:sum(g[A][j]!=0 for A in range(A)));F=[g[A][B]for A in range(A)if g[A][B]];I=next(A for A in range(A)if g[A][B]);g[C]=[D[(A-H)%len(D)]for A in range(E)]
	for G in range(A):g[G][B]=F[(G-I)%len(F)]
	return g