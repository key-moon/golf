def p(A):
	for B in A:
		for C in B:
			if C:
				for D in range(B.index(C),len(B)-1-B[::-1].index(C)+1):B[D]=C
	return A