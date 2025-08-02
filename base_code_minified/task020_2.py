def p(g):
	C=min(B for A in g for(B,C)in enumerate(A)if C);D=max(B for A in g for(B,C)in enumerate(A)if C);E=(C+D)//2
	for A in g:
		for(F,B)in enumerate(A):
			if B:A[2*E-F]=B
	return g