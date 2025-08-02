def p(A):
	for(D,E)in enumerate(A):
		if 2 in E:F,B=E.index(2),D
		if 3 in E:C,G=E.index(3),D
	if F>C:F,C=C,F
	if B>G:B,G=G,B
	for H in range(F,C+1):
		if A[B][H]<1:A[B][H]=8
	for D in range(B,G+1):
		if A[D][C]<1:A[D][C]=8
	return A