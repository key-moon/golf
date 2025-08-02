def p(A):
	B=len(A)//3;C=len(A[0])//3
	for F in range(3):
		for G in range(3):
			if all(A[F*B+D][G*C+E]for D in range(B)for E in range(C)):H,I=F*B,G*C
	for D in range(len(A)):
		for E in range(len(A[0])):
			if A[D][E]==0:A[D][E]=A[H+D%B][I+E%C]
	return A