def p(A):
	B=0
	while any(A[B]):B+=1
	for C in range(B):A[-C-1]=A[C]
	return A