def p(A):
	F,G=len(A),len(A[0]);E=()
	for B in range(1,F-1):
		for C in range(1,G-1):
			D=A[B][C]
			if D and A[B-1][C]==D==A[B+1][C]and A[B][C-1]==D==A[B][C+1]:E+=(B,C),
	for(B,C)in E:A[B][C]=0
	return A