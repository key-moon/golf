def p(A):
	E=range(8)
	for B in E:
		for C in E:
			for D in E[C+1:]:
				if A[B][C]==A[B][D]!=0 and not C+D&1:A[B][C+D>>1]=A[B][C]
	for B in E:
		for C in E:
			for D in E[B+1:]:
				if A[B][C]==A[D][C]!=0 and not B+D&1:A[B+D>>1][C]=A[B][C]
	return A