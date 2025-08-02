def p(g):
	E={}
	for(A,L)in enumerate(g):
		for(B,I)in enumerate(L):
			if I:E.setdefault(I,[]).append((A,B))
	F={}
	for(D,G)in E.items():
		if len(G)>1:
			J,M=G[0]
			if all(A==J for(A,B)in G):F[D]='h',J
			else:F[D]='v',M
	for(D,(K,C))in F.items():
		for(A,B)in E[D]:
			if K=='v'and B!=C:H=(B>C)-(B<C);g[A][C+H]=D;g[A][B]=0
			if K=='h'and A!=C:H=(A>C)-(A<C);g[C+H][B]=D;g[A][B]=0
	return g