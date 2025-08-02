def p(A):
	for D in range(9):
		for E in range(9):
			if A[D][E]==2:
				for(F,G)in((-1,-1),(-1,1),(1,-1),(1,1)):
					B=D+F;C=E+G
					if 0<=B<9 and 0<=C<9:A[B][C]=4
			if A[D][E]==1:
				for(F,G)in((-1,0),(1,0),(0,-1),(0,1)):
					B=D+F;C=E+G
					if 0<=B<9 and 0<=C<9:A[B][C]=7
	return A