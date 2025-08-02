def p(g):
	E={A for B in g for A in B if A}
	for B in E:
		A=[(A,D)for(A,C)in enumerate(g)for(D,E)in enumerate(C)if E==B];F=min(A for(A,B)in A);G=max(A for(A,B)in A);C=min(A for(B,A)in A);D=max(A for(B,A)in A)
		for H in range(F,G+1):g[H][C:D+1]=[B]*(D-C+1)
	return g