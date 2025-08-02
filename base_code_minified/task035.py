def p(g):
	D=min(A for(A,B)in enumerate(g)for(D,C)in enumerate(B)if C==8);H=max(A for(A,B)in enumerate(g)for(D,C)in enumerate(B)if C==8);E=min(B for A in g for(B,C)in enumerate(A)if C==8);F=max(B for A in g for(B,C)in enumerate(A)if C==8)
	for(G,B)in enumerate(g):
		for(C,A)in enumerate(B):
			if A and A!=8:
				if C<E:B[E]=A
				elif C>F:B[F]=A
				elif G<D:g[D][C]=A
	return g