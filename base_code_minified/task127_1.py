def p(g):
	C=[-1]+[A for A in range(len(g))if g[A]==[5]*len(g[0])]+[len(g)];D=[-1]+[A for A in range(len(g[0]))if all(g[B][A]==5 for B in range(len(g)))]+[len(g[0])]
	for(E,F)in zip(C,C[1:]):
		for(A,B)in zip(D,D[1:]):
			G=sum(g[C][D]for C in range(E+1,F)for D in range(A+1,B))+5
			for H in range(E+1,F):g[H][A+1:B]=[G]*(B-A-1)
	return g