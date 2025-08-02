def p(g):
	Q,M=len(g),len(g[0]);D=[B for(B,A)in enumerate(g)if A.count(A[0])==M];N=g[D[0]][0];F=[A for A in range(M)if g[D[0]][A]==N];G,H=len(D)-1,len(F)-1;E=[[g[D[A]+1][F[B]+1]for B in range(H)]for A in range(G)]
	for C in{B for A in E for B in A}-{0}:
		for A in range(G):
			I=[B for B in range(H)if E[A][B]==C]
			if len(I)>1:
				J,K=min(I),max(I)
				for B in range(J+1,K):E[A][B]=C
		for B in range(H):
			L=[A for A in range(G)if E[A][B]==C]
			if len(L)>1:
				J,K=min(L),max(L)
				for A in range(J+1,K):E[A][B]=C
	for A in range(G):
		for B in range(H):
			C=E[A][B]
			if C:
				for O in range(D[A]+1,D[A+1]):
					for P in range(F[B]+1,F[B+1]):g[O][P]=C
	return g