def p(A):
	for(D,C)in enumerate(A):
		for(B,E)in enumerate(C):
			if E==2 and not(D and A[D-1][B]==2 or D<len(A)-1 and A[D+1][B]==2 or B and C[B-1]==2 or B<len(C)-1 and C[B+1]==2):C[B]=1
	return A