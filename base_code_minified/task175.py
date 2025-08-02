def p(g):
	from collections import Counter as D;E,F=len(g),len(g[0])
	for A in range(E):
		for B in range(F):
			if g[A][B]==0:G=[g[A+C][B+D]for C in(-1,0,1)for D in(-1,0,1)if C|D if 0<=A+C<E and 0<=B+D<F if g[A+C][B+D]];C=D(G).most_common();g[A][B]=C[1][0]if len(C)>1 else C[0][0]
	return g