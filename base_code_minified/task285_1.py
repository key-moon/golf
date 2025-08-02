def p(A):
	F={A for B in A for A in B if A}
	for C in F:
		B=[(A,D)for(A,B)in enumerate(A)for(D,E)in enumerate(B)if E==C];G=min(A for(A,B)in B);H=max(A for(A,B)in B);D=min(A for(B,A)in B);E=max(A for(B,A)in B)
		for I in range(G,H+1):A[I][D:E+1]=[C]*(E-D+1)
	return A