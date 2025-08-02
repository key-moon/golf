def p(g):
	E=len(g);C=max({A for B in g for A in B if A},key=lambda x:sum(A.count(x)for A in g));A=[(B,E)for(B,D)in enumerate(g)for(E,A)in enumerate(D)if A and A!=C]
	if not A:return g
	F=min(A for(A,B)in A);G=max(A for(A,B)in A);H=min(A for(B,A)in A);I=max(A for(B,A)in A)
	for B in range(E):
		for J in range(E):g[B][J]=0
	for D in range(G-F+1):B=F+D;g[B][H+D]=C;g[B][I-D]=C
	return g