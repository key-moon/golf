def p(A):
	B=3;C=0
	while C<B and any(A[C][B]for B in range(B)):C+=1
	D=0
	while D<B and any(A[B][D]for B in range(B)):D+=1
	E=[[0]*(B*D)for A in range(B*C)]
	for H in range(C):
		for F in range(D):
			for G in range(B):E[H*B+G][F*B:F*B+B]=A[G][:]
	return E