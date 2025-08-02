def p(A):
	D=[-1]+[B for B in range(len(A))if A[B]==[5]*len(A[0])]+[len(A)];E=[-1]+[B for B in range(len(A[0]))if all(A[C][B]==5 for C in range(len(A)))]+[len(A[0])]
	for(F,G)in zip(D,D[1:]):
		for(B,C)in zip(E,E[1:]):
			H=sum(A[D][E]for D in range(F+1,G)for E in range(B+1,C))+5
			for I in range(F+1,G):A[I][B+1:C]=[H]*(C-B-1)
	return A