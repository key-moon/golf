def p(A):
	for C in range(len(A)):
		for D in range(len(A[0])):
			if not A[C][D]:
				for B in range(1,len(A)):
					if C+B<len(A)and D+B<len(A[0])and A[C+B][D+B]:A[C][D]=A[C+B][D+B];break
					if C>=B and D>=B and A[C-B][D-B]:A[C][D]=A[C-B][D-B];break
	return A