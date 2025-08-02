def p(A):
	for(F,E)in enumerate(A):
		for B in range(len(E)):
			if E[B]and(F<1 or not A[F-1][B])and(B<1 or not E[B-1]):
				C=B
				while C<len(E)and E[C]:C+=1
				D=F
				while D<len(A)and all(A[D][B]for B in range(B,C)):D+=1
				if(D==len(A)or all(not A[D][B]for B in range(B,C)))and(C==len(E)or all(not A[B][C]for B in range(F,D))):return[A[D][B:C]for D in range(F,D)]
	return A