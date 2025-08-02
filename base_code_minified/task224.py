def p(g):
	A,B=zip(*[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==5]);C,D=min(A)+1,max(A)-1;E,F=min(B)+1,max(B)-1;G=next(A for B in g for A in B if A%5)
	for H in range(E,F+1):g[C][H]=g[D][H]=G
	for I in range(C,D+1):g[I][E]=g[I][F]=G
	return g