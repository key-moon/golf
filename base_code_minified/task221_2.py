def p(A):
	D=len(A);C=len(A[0]);B=sum(B==0 for A in A for B in A);F=[[0]*C*B for A in range(D*B)]
	for E in range(D*C-B):
		for(G,H)in enumerate(A):F[D*(E//B)+G][C*(E%B):C*(E%B)+C]=H
	return F