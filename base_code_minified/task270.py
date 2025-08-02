def p(g):
	D=[[0]*15 for A in[0]*15]
	for A in range(15):
		for B in range(15):
			E=g[A][B]
			if 0<E<3:
				D[A][B]=E;H=sorted([C for C in range(15)if g[A][C]>E and C<B],reverse=1)
				for(C,F)in enumerate(H):D[A][B-C-1]=g[A][F]
				I=sorted([C for C in range(15)if g[A][C]>E and C>B])
				for(C,F)in enumerate(I):D[A][B+C+1]=g[A][F]
				J=sorted([C for C in range(15)if g[C][B]>E and C<A],reverse=1)
				for(C,G)in enumerate(J):D[A-C-1][B]=g[G][B]
				K=sorted([C for C in range(15)if g[C][B]>E and C>A])
				for(C,G)in enumerate(K):D[A+C+1][B]=g[G][B]
	return D