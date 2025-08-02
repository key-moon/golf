def p(g):
	C,D=len(g),len(g[0]);K={*g[0],*g[-1],*(A[0]for A in g),*(A[-1]for A in g)}-{0};E,F=K
	for A in range(1,C):
		if g[A][0]!=E:G=A;break
	for A in range(1,C):
		if g[A][-1]!=E:H=A;break
	for B in range(1,D):
		if g[0][B]!=F:I=B;break
	for B in range(1,D):
		if g[-1][B]!=F:J=B;break
	for A in range(min(G,H),max(G,H)+1):
		for B in range(min(I,J),max(I,J)+1):
			if g[A][B]==0:g[A][B]=3
	return g