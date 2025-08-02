def p(A):
	B=len(A);F,G=next((C,D)for C in range(B-1)for D in range(B-1)if A[C][D]and A[C][D]==A[C][D+1]==A[C+1][D]==A[C+1][D+1]);H=A[F][G]
	for C in range(B):
		for D in range(B):
			if A[C][D]==H and not(F<=C<=F+1 and G<=D<=G+1):
				I=1 if C>F else-1;J=1 if D>G else-1;E=1
				while 0<=C+E*I<B and 0<=D+E*J<B:A[C+E*I][D+E*J]=H;E+=1
	return A