def p(g):
	D=next(A[0]for A in g if A.count(A[0])==len(A)and A[0])
	for(H,A)in enumerate(g):
		for B in{*A}-{0,D}:
			C=[A for(A,C)in enumerate(A)if C==B];E,F=min(C),max(C)
			for G in range(E,F+1):A[G]=B
	return g