def p(A):
	C=list(zip(*[A[:3]for A in A][::-1]));D=list(zip(*C[::-1]))
	for B in(0,1,2):A[B][4:7]=C[B];A[B][8:]=D[B]
	return A