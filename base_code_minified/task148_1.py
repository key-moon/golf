def p(g):
	C=min(A for A in range(len(g[0]))if any(g[B][A]==2 for B in range(len(g))));D=max(A for A in range(len(g[0]))if any(g[B][A]==2 for B in range(len(g))));G=min(A for A in range(len(g))if g[A][C]==2);H=min(A for A in range(len(g))if g[A][D]==2);I=H-G;J=[(A,B)for A in range(len(g))for B in range(len(g[0]))if g[A][B]==8]
	for(B,E)in J:
		g[B][E]=4
		for A in range(C,E):
			if g[B][A]==0:g[B][A]=8
		F=B+I
		for A in range(C,D):
			if g[F][A]==0:g[F][A]=8
	return g