def p(g):
	A=min(A for(A,B)in enumerate(g)for C in B if C==1);B=max(A for(A,B)in enumerate(g)for C in B if C==1);C=min(B for A in g for(B,C)in enumerate(A)if C==1);D=max(B for A in g for(B,C)in enumerate(A)if C==1);H=[A[C:D+1]for A in g[A:B+1]];I=(B-A)//2;J=(D-C)//2
	for(E,K)in enumerate(g):
		for(F,L)in enumerate(K):
			if L==4 and not(A<=E<=B and C<=F<=D):
				for(M,N)in enumerate(H):
					for(O,G)in enumerate(N):
						if G:g[E-I+M][F-J+O]=G
	return g