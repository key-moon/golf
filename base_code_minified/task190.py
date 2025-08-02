def p(g):
	A,B=next((A,B)for A in range(9)for B in range(9)if g[A][B]==g[A][B+1]==g[A+1][B]==g[A+1][B+1]and g[A][B]);G=g[A][B]
	for C in range(10):
		for D in range(10):
			if g[C][D]==G and not(A<=C<=A+1 and B<=D<=B+1):
				H=(C>A+1)-(C<A);I=(D>B+1)-(D<B);E,F=C+H,D+I
				while 0<=E<10 and 0<=F<10:g[E][F]=G;E+=H;F+=I
	return g