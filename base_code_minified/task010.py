def p(A):
	B={}
	for D in A:
		for(C,E)in enumerate(D):
			if E==5 and C not in B:B[C]=len(B)+1
	return[[B[A]if C==5 else 0 for(A,C)in enumerate(A)]for A in A]