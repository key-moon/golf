def p(A):
	E,F=len(A),len(A[0])
	for D in range(E):
		for C in range(F):
			for B in range(3,min(E-D,F-C)+1):
				if A[D][C:C+B]==[5]*B==A[D+B-1][C:C+B]and all(A[D+E][C:C+B:B-1]==[5,5]for E in range(B)):
					for G in range(D+1,D+B-1):
						for H in range(C+1,C+B-1):A[G][H]=B+3
	return A