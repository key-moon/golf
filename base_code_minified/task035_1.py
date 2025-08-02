def p(g):
	D=[A for(A,B)in enumerate(g)for C in B if C==8];E=[B for A in g for(B,C)in enumerate(A)if C==8];F,G=min(D),max(D);H,I=min(E),max(E)
	for(B,J)in enumerate(g):
		for(C,A)in enumerate(J):
			if A%8:
				if C<H:g[B][H]=A
				elif C>I:g[B][I]=A
				elif B<F:g[F][C]=A
				elif B>G:g[G][C]=A
	return g