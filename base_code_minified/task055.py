def p(g):
	E,C=len(g),len(g[0]);F,H=[A for(A,B)in enumerate(g)if B==[8]*C];D,G=[A for A in range(C)if[B[A]for B in g]==[8]*E]
	for B in range(E):
		for A in range(C):
			if g[B][A]==0:
				if F<B<H:g[B][A]=6 if D<A<G else 4 if A<D else 3
				elif D<A<G:g[B][A]=2 if B<F else 1
	return g