def p(g):
	B={(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==1}
	while B:
		I=B.pop();A={I};D=[I]
		while D:
			J,K=D.pop()
			for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
				C=J+L,K+M
				if C in B:B.remove(C);A.add(C);D.append(C)
		E,F=min(A for(A,B)in A),max(A for(A,B)in A);G,H=min(A for(B,A)in A),max(A for(B,A)in A);N={(E,A)for A in range(G,H+1)}|{(F,A)for A in range(G,H+1)}|{(A,G)for A in range(E,F+1)}|{(A,H)for A in range(E,F+1)}
		if A==N:
			for(O,P)in A:g[O][P]=8
	return g