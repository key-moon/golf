def p(A):
	D,E=len(A),len(A[0]);J=[(B,A[B][0])for B in range(D)if A[B][0]and A[B].count(A[B][0])==E];K=[(B,A[0][B])for B in range(E)if A[0][B]and sum(A[C][B]==A[0][B]for C in range(D))==D];F=[[0]*E for A in range(D)]
	for(C,B)in J:F[C]=[B]*E
	for(G,B)in K:
		for C in range(D):F[C][G]=B
	for C in range(D):
		for G in range(E):
			H=A[C][G]
			if not H:continue
			for(I,B)in J:
				if H==B and C!=I:F[I+(-1 if C<I else 1)][G]=B
			for(L,B)in K:
				if H==B and G!=L:F[C][L+1]=B
	return F