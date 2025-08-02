def p(A):
	for B in A:
		for C in range(len(B)-2):
			if B[C]==B[C+2]==1 and not B[C+1]:B[C+1]=2
	return A