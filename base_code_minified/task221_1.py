def p(g):
	A=3;B=0
	while B<A and any(g[B][A]for A in range(A)):B+=1
	C=0
	while C<A and any(g[A][C]for A in range(A)):C+=1
	D=[[0]*(A*C)for B in range(A*B)]
	for G in range(B):
		for E in range(C):
			for F in range(A):D[G*A+F][E*A:E*A+A]=g[F][:]
	return D