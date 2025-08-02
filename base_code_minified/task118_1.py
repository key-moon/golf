def p(g):
	for A in g:
		if 2 in A:
			C=A.index(2);D=len(A)-A[::-1].index(2)-1
			for B in range(C+1,D):
				if A[B]!=2:A[B]=8
	return g