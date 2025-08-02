def p(g):
	A=next(A for(A,B)in enumerate(g)if B[0]!=g[0][0]);B=next(A for(A,B)in enumerate(g[0])if B!=g[0][0]);D=[g[0][0],g[0][B],g[A][0],g[A][B]];C=[0,0,0,0]
	for(F,G)in enumerate(g):
		for(H,I)in enumerate(G):E=(F>=A)<<1|(H>=B);C[E]+=I!=D[E]
	return[[D[C.index(max(C))]]]