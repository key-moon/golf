def p(g):
	B=next(A for(A,B)in enumerate(g[9])if B);E=g[9][B]
	for(C,F)in enumerate(g):
		for D in range(10):A=D-B;F[D]=(C<1 and A&3==1 or C==9 and A&3==3)and 5 or E*(A&1^1)
	return g