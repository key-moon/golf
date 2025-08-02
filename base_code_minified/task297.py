def p(A):
	B=A[0];C=len(B)
	for D in range(len(A)-2):A[D+2]=C*[B[D%C]]
	return A