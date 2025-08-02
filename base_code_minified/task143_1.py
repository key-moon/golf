def p(g):
	B=[A for B in g for A in B if A];C=[A for A in set(B)if B.count(A)==7][0];A=[(A,B)for A in range(10)for B in range(10)if g[A][B]==C];G,H=min(A for(A,B)in A),min(A for(B,A)in A);A=[(A-G,B-H)for(A,B)in A]
	for I in set(B)-{C}:
		E=[(A,B)for A in range(10)for B in range(10)if g[A][B]==I];J,K=min(A for(A,B)in E),min(A for(B,A)in E)
		for(L,M)in A:
			F,D=J+L,K+M
			if 0<=F<10<D<10 or 0<=D<10:g[F][D]=C
	return g