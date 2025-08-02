def p(A):
	for B in A:
		for C in range(len(B)-2):
			if B[C]and B[C]==B[C+1]==B[C+2]:A[-1][C+1]=4
	return A