def p(A):
	for B in A:
		if 8 in B:
			F=B.index(8);G=len(B)-1-B[::-1].index(8)
			for H in range(F,G+1):B[H]=8
	D=range(len(A))
	for E in D:
		C=[B for B in D if A[B][E]==8]
		if C:
			for I in range(C[0],C[-1]+1):A[I][E]=8
	return A