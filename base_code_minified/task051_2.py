def p(g):
	G=[A for B in g for A in B if A];C=next(A for A in set(G)if G.count(A)==1)
	for(I,H)in enumerate(g):
		if C in H:A,B=I,H.index(C);break
	J=sum(g[A][B]==0 for A in range(A));K=sum(g[A][B]==0 for A in range(A+1,len(g)));L=sum(g[A][B]==0 for B in range(B));M=sum(g[A][B]==0 for B in range(B+1,len(g[0])));F=max((J,'u'),(K,'d'),(L,'l'),(M,'r'))[1]
	if F=='u':
		for D in range(A):
			if g[D][B]==0:g[D][B]=C
	if F=='d':
		for D in range(A+1,len(g)):
			if g[D][B]==0:g[D][B]=C
	if F=='l':
		for E in range(B):
			if g[A][E]==0:g[A][E]=C
	if F=='r':
		for E in range(B+1,len(g[0])):
			if g[A][E]==0:g[A][E]=C
	return g