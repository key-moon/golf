def p(g):
	B=len(g);D=len(g[0]);A=[0]*D
	for C in range(D):
		while A[C]<B and g[B-1-A[C]][C]==5:A[C]+=1
	G=[A for A in A if A];E=max(A);F=min(G);H=A.index(E);I=A.index(F);return[[1 if C==H and A>=B-E else 2 if C==I and A>=B-F else 0 for C in range(D)]for A in range(B)]