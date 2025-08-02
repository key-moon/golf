def p(g):
	B=next(A for B in g for A in B if A and sum(C==A for B in g for C in B)==1);C,D=next((A,D)for(A,C)in enumerate(g)for(D,E)in enumerate(C)if E==B);H,E=len(g),len(g[0]);A=[[0]*E for A in g]
	for I in(-1,0,1):
		for J in(-1,0,1):
			F,G=C+I,D+J
			if 0<=F<H and 0<=G<E:A[F][G]=2
	A[C][D]=B;return A