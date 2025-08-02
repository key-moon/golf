def p(A):
	E=next(A[0]for A in A if A.count(A[0])==len(A)and A[0])
	for(I,B)in enumerate(A):
		for C in{*B}-{0,E}:
			D=[A for(A,B)in enumerate(B)if B==C];F,G=min(D),max(D)
			for H in range(F,G+1):B[H]=C
	return A