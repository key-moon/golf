def p(A):
	for B in range(1,len(A)-1):
		for C in range(1,len(A)-1):
			D=A[B-1][C]
			if D==A[B+1][C]==A[B][C-1]==A[B][C+1]!=A[B][C]:A[B][C]=D;return[[A[B][C]for C in(C-1,C,C+1)]for B in(B-1,B,B+1)]