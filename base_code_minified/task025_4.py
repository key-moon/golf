def p(g):
	for F in{A for B in g for A in B if A}:
		C=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==F];G=[A for(A,B)in C];H=[A for(B,A)in C];D=max(set(G),key=G.count);E=max(set(H),key=H.count)
		if G.count(D)>H.count(E):
			for(A,B)in C:
				if A!=D:g[D+(1 if A>D else-1)][B]=F;g[A][B]=0
		else:
			for(A,B)in C:
				if B!=E:g[A][E+(1 if B>E else-1)]=F;g[A][B]=0
	return g