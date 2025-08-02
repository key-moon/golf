def p(g):
	C=len(g);D=sorted((B,D,A)for(B,C)in enumerate(g)for(D,A)in enumerate(C)if A);E,I,F=D[0];G,I,H=D[-1]
	for B in range(1,C-1):g[B][0]=g[B][-1]=F if B*2<=E+G else H
	for A in range(C):g[0][A]=g[E][A]=F;g[G][A]=g[-1][A]=H
	return g