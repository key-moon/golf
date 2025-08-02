def p(g):
	A={}
	for C in g:
		for(B,D)in enumerate(C):
			if D==5 and B not in A:A[B]=len(A)+1
	return[[A[B]if C==5 else 0 for(B,C)in enumerate(B)]for B in g]