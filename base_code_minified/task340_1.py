def p(A):
	E,F,G,H=A[0][1],A[-1][1],A[1][0],A[1][-1]
	for B in range(1,len(A)-1):
		for C in range(1,len(A[0])-1):
			D=A[B][C]
			if D==E:A[1][C]=E
			elif D==F:A[-2][C]=F
			elif D==G:A[B][1]=G
			elif D==H:A[B][-2]=H
			A[B][C]=0
	return A