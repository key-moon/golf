def p(A):
	for B in range(len(A)-2):
		for C in range(len(A[0])-2):
			D=A[B][C];E=A[B+1][C+1]
			if D and E!=D and all(A[B+E][C+F]==D for(E,F)in((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2))):return[[E]]