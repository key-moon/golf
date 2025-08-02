def p(g):
	F=len(g);G=len(g[0]);H=(F-1)/2;I=(G-1)/2;J={}
	for A in range(F):
		for B in range(G):
			if g[A][B]:J.setdefault(g[A][B],[]).append((A,B))
	for(K,C)in J.items():
		L=[A for(A,B)in C];M=[A for(B,A)in C];N,O=min(L),max(L);P,Q=min(M),max(M);R,S=(N+O)//2,(P+Q)//2
		if g[R][S]==K:
			for(A,B)in C:
				D=A-H;E=B-I
				for(T,U)in((-E,D),(-D,-E),(E,-D)):g[int(H+T)][int(I+U)]=K
	return g