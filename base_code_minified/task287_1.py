def p(A):
	B=len(A[0])//2
	for C in A:C[B:]=C[:B][::-1]
	return A