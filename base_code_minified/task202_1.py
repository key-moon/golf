def p(A):
	B=0
	while B<len(A):
		D=next(A for A in A[B]if A);C=B
		while C<len(A)and next(A for A in A[C]if A)==D:C+=1
		E={B for A in A[B:C]for(B,C)in enumerate(A)if C<1}
		for F in A[B:C]:
			for G in E:F[G]=0
		B=C
	return A