def p(g):
	A=[(A,B)for A in range(len(g))for B in range(len(g[0]))if g[A][B]==5]
	if not A:return g
	B=min(A for(A,B)in A);C=min(A for(B,A)in A);D=sum(1 for(A,D)in A if D-C<=A-B);G=len(A)-D;H,I=(2,8)if G>D else(8,2)
	for(E,F)in A:g[E][F]=H if F-C<=E-B else I
	return g