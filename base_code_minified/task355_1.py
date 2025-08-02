def p(A):
	E,F=len(A),len(A[0]);D=A[0][0]
	for B in range(F):
		if A[0][B]!=D:break
	for C in range(E):
		if A[C][0]!=D:break
	I,J=D,sum(A[C][E]!=D for C in range(C)for E in range(B))
	for(G,H,L,M)in((0,B,C,F),(C,0,E,B),(C,B,E,F)):
		K=sum(A[B][C]!=A[G][H]for B in range(G,L)for C in range(H,M))
		if K>J:I,J=A[G][H],K
	return I