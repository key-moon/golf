def p(g):
	D=[A for(A,B)in enumerate(g)for C in B if C==2];E=[B for A in g for(B,C)in enumerate(A)if C==2];F,G=min(D),max(D);H,I=min(E),max(E);C=[[0]*len(g[0])for A in g]
	for(A,K)in enumerate(g):
		for(B,J)in enumerate(K):
			if J==2:C[A][B]=2
			if J==5:L=F-1 if A<F else G+1 if A>G else A;M=H-1 if B<H else I+1 if B>I else B;C[L][M]=5
	return C