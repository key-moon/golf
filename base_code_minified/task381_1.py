def p(A):
	for B in A:
		if 2 in B:
			D=B.index(2);E=len(B)-1-B[::-1].index(2)
			for C in range(D+1,E):
				if not B[C]:B[C]=9
	return A