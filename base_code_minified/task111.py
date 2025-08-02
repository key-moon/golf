def p(g):
	for(A,B)in enumerate(g):
		if 5 in B:C=B.index(5);break
	return[A[C-1:C+2]for A in g[A+1:A+4]]