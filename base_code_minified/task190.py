def p(A):
	B,C=next((B,C)for B in range(9)for C in range(9)if A[B][C]==A[B][C+1]==A[B+1][C]==A[B+1][C+1]and A[B][C]);H=A[B][C]
	for D in range(10):
		for E in range(10):
			if A[D][E]==H and not(B<=D<=B+1 and C<=E<=C+1):
				I=(D>B+1)-(D<B);J=(E>C+1)-(E<C);F,G=D+I,E+J
				while 0<=F<10 and 0<=G<10:A[F][G]=H;F+=I;G+=J
	return A