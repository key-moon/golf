def p(g):
	A=len(g);B=len(g[0]);F=A//3;C=max(range(A),key=lambda y:sum(g[y][A]==8 for A in range(B)));G=[A for A in range(B)if g[C][A]==8]
	for H in(1,2):
		for D in G:
			E=C+H*F
			if g[E][D]==0:g[E][D]=1
	return g