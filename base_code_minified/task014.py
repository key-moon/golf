def p(g):
	A={}
	for(E,F)in enumerate(g):
		for C in F:
			if C and C not in A:A[C]=E
	D=max(A,key=A.get);B=[(A,C)for(A,B)in enumerate(g)for(C,E)in enumerate(B)if E==D];G=min(A for(A,B)in B);H=max(A for(A,B)in B);I=min(A for(B,A)in B);J=max(A for(B,A)in B);return[[D if g[A][B]==D else 0 for B in range(I,J+1)]for A in range(G,H+1)]