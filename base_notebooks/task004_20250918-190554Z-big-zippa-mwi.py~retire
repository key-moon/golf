def p(g,p=enumerate):
	A=[[0]*len(g[0])for A in g]
	for B in{*sum(g,[])}-{0}:
		C=[(A,D)for(A,C)in p(g)for(D,E)in p(C)if E==B];F,G=map(max,zip(*C))
		for(D,E)in C:A[D][E+(D<F)*(E<G)]=B
	return A