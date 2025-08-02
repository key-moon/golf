def p(A):
	for B in len(A)>3 and[A[B:B+3]for B in range(0,len(A),3)]or[[A[B:B+3]for A in A]for B in range(0,len(A[0]),3)]:
		if B==[A[::-1]for A in B[::-1]]:return B