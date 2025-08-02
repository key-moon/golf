def p(A):
	D=[(B,set(A)-{0})for(B,A)in enumerate(A)if set(A)-{0}];E=[[D[0][0]]];B=D[0][1]
	for(H,C)in D[1:]:E[-1].append(H)if C==B else E.append([H]);B=C
	I,K=len(A),len(A[0]);F=[(B,set(A[C][B]for C in range(I))-{0})for B in range(K)if set(A[C][B]for C in range(I))-{0}];G=[[F[0][0]]];B=F[0][1]
	for(J,C)in F[1:]:G[-1].append(J)if C==B else G.append([J]);B=C
	return[[next(A[B][C]for B in B for C in D if A[B][C])for D in G]for B in E]