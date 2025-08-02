def p(A):
	if len(A)<len(A[0]):
		for D in range(len(A[0])):
			E=[A[D]for A in A];C=max(E,key=E.count)
			for B in A:B[D]=C
		for B in A:C=max(B,key=B.count);B[:]=[C]*len(B)
	return A