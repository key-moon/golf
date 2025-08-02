def p(A):
	J,G=len(A),len(A[0]);H=[[0]*G for A in A]
	for B in range(2,J-2):
		for C in range(2,G-2):
			I=A[B][C];D=A[B-1][C]
			if I and D and A[B+1][C]==D==A[B][C-1]==A[B][C+1]:
				for(E,F)in((2,0),(1,0),(0,1),(0,2),(-1,0),(0,-1),(0,-2),(-2,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,0)):H[B+E][C+F]=D if E*F==0 and(E or F)else I
	return H