def p(A):
	D=[A[:]for A in A]
	for C in range(len(A)-2):
		for B in range(len(A[0])-2):
			if A[C][B:B+3]==[1,1,1]and A[C+1][B:B+3]==[1,0,1]and A[C+2][B:B+3]==[1,1,1]:
				for(E,F)in((0,1),(1,0),(1,1),(1,2),(2,1)):D[C+E][B+F]=2
				for(E,F)in((0,0),(0,2),(2,0),(2,2)):D[C+E][B+F]=0
	return D