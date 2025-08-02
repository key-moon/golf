def p(A):
	for B in(0,3,6):
		if not A[B][0]==A[B+1][1]==A[B+2][2]:return A[B:B+3]