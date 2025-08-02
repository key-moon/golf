def p(A):
	A[0]=A[-1]=[8]*len(A[0])
	for B in A[1:-1]:B[0]=B[-1]=8
	return A