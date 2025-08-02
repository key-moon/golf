def p(A):
	for B in range(2,len(A)-2):
		for C in range(2,len(A)-2):
			E=A[B][C]
			if E and A[B-1][C]==A[B+1][C]==A[B][C-1]==A[B][C+1]!=E:
				F=A[B-1][C]
				for D in(1,2,-1,-2):A[B+D][C]=F;A[B][C+D]=F;A[B+D][C+D]=E;A[B+D][C-D]=E
	return A