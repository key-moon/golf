def p(g):
	for(C,H)in enumerate(g):
		for(D,E)in enumerate(H):
			if E==3:A,B=C,D
			if E==4:F,G=C,D
	I=(F>A)-(F<A);J=(G>B)-(G<B);g[A][B]=0;g[A+I][B+J]=3;return g