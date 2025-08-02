def p(A):
	D=[[0]*3 for A in[0]*3]
	for B in range(len(A)-1):
		for C in range(len(A[0])-1):
			if A[B][C]==2==A[B+1][C]==A[B][C+1]==A[B+1][C+1]:D[B//2][C//2]=1
	return D