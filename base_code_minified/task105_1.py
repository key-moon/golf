def p(A):
	for(C,D)in enumerate(A):
		for(B,E)in enumerate(D):
			if not E and 1 in D[:B]and 1 in D[B+1:]or 1 in[A[B]for A in A[:C]]and 1 in[A[B]for A in A[C+1:]]:A[C][B]=2
	return A