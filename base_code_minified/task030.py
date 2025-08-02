def p(g):
	B={}
	for(C,D)in enumerate(g):
		for(E,A)in enumerate(D):
			if A:B[A]=min(B.get(A,len(g)),C)
	G=B[1];F=[[0]*len(A)for A in g]
	for(C,D)in enumerate(g):
		for(E,A)in enumerate(D):
			if A:F[C-B[A]+G][E]=A
	return F