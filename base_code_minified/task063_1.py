def p(A):
	D,E=len(A),len(A[0]);L={*A[0],*A[-1],*(A[0]for A in A),*(A[-1]for A in A)}-{0};F,G=L
	for B in range(1,D):
		if A[B][0]!=F:H=B;break
	for B in range(1,D):
		if A[B][-1]!=F:I=B;break
	for C in range(1,E):
		if A[0][C]!=G:J=C;break
	for C in range(1,E):
		if A[-1][C]!=G:K=C;break
	for B in range(min(H,I),max(H,I)+1):
		for C in range(min(J,K),max(J,K)+1):
			if A[B][C]==0:A[B][C]=3
	return A