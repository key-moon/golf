def p(A):
	B=A[-1][0];C=min(A for B in A for A in B if A)
	for(D,E)in enumerate(A):
		for(F,G)in enumerate(E):
			if G==C:A[D][F]=B
	A[-1][0]=0;return A