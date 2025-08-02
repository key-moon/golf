def p(A):
	for(B,C)in enumerate(A):
		if 5 in C:D=C.index(5);break
	return[A[D-1:D+2]for A in A[B+1:B+4]]