def p(g):
	B=g[0][0];J=next(A for C in g for A in C if A and A!=B);A=[(A,D)for(A,C)in enumerate(g)for(D,E)in enumerate(C)if E==B];C=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==J];D=[A for(A,B)in A];K=[A for(B,A)in A];L=[A for(A,B)in C];E=[A for(B,A)in C];M,F=min(D)+1,max(D);G,N=min(K)-1,max(E);O=max(L)
	for H in range(M,O):
		if 0==g[H][G]:g[H][G]=3
	for I in range(min(E)+1,N):
		if 0==g[F][I]:g[F][I]=3
	return g