def p(g):
	H,I=len(g),len(g[0]);G={};M={A for B in g for A in B if A not in(0,5)}
	for E in M:
		F=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==E];N=min(A for(A,B)in F);O=min(A for(B,A)in F);P=tuple(sorted((A-N,B-O)for(A,B)in F));G[P]=E
		for(A,B)in F:g[A][B]=0
	for A in range(H):
		for B in range(I):
			if g[A][B]==5 and(A==0 or g[A-1][B]!=5)and(B==0 or g[A][B-1]!=5):
				C=1
				while B+C<I and g[A][B+C]==5:C+=1
				D=1
				while A+D<H and all(g[A+D][B+C]==5 for C in range(C)):D+=1
				J=tuple(sorted((D-A,E-B)for D in range(A,A+D)for E in range(B,B+C)if g[D][E]!=5))
				if J in G:
					E=G[J]
					for K in range(A,A+D):
						for L in range(B,B+C):
							if g[K][L]!=5:g[K][L]=E
	return g