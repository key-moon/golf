def p(g):
	E=[(A,B)for A in range(len(g))for B in range(len(g[0]))if g[A][B]];A,B=min(E);C,D=max(E);F=g[A][B];G=[g[A][B]for(A,B)in E if g[A][B]!=F][0]
	for(J,K,L)in((A,B,G),(A,D,F),(C,B,F),(C,D,G)):
		for M in(-1,0,1):
			for N in(-1,0,1):g[J+M][K+N]=L
	for H in range(B+2,D-1,2):g[A][H]=g[C][H]=5
	for I in range(A+2,C-1,2):g[I][B]=g[I][D]=5
	return g