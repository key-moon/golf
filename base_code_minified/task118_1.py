def p(A):
	for B in A:
		if 2 in B:
			D=B.index(2);E=len(B)-B[::-1].index(2)-1
			for C in range(D+1,E):
				if B[C]!=2:B[C]=8
	return A