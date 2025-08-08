def p(g,P=range):
	D=[A[:]for A in g]
	for H in P(1,10):
		B=[(A,B)for A in P(len(g))for B in P(len(g[0]))if g[A][B]==H]
		for G in P(len(B)):
			for I in P(G+1,len(B)):
				A,E=B[G];C,F=B[I]
				if A==C:
					for J in P(min(E,F),max(E,F)+1):D[A][J]=8
				elif E==F:
					for K in P(min(A,C),max(A,C)+1):D[K][E]=8
		for(A,C)in B:D[A][C]=1
	return D