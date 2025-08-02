def p(A):
	for C in range(len(A)-1):
		for B in range(len(A[0])-1):
			if A[C][B:B+2]==[5,5]and A[C+1][B:B+2]==[5,5]:A[C-1][B-1],A[C-1][B+2],A[C+2][B-1],A[C+2][B+2]=1,2,3,4
	return A