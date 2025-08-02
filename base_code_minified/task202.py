def p(A):
	J,K=len(A),len(A[0]);L=[(B,C)for B in range(J)for C in range(K)if A[B][C]==0]
	for H in set(sum(A,[]))-{0}:
		I=[B for B in range(J)if H in A[B]];M=[B for B in range(K)if any(A[C][B]==H for C in I)];B,C=I[0],I[-1];D,E=M[0],M[-1];N={A for(A,F)in L if B<=A<=C and D<=F<=E};O={A for(F,A)in L if B<=F<=C and D<=A<=E}
		if O and E-D>C-B:
			for F in range(B,C+1):
				for G in O:
					if A[F][G]==H:A[F][G]=0
		if N and C-B>=E-D:
			for F in N:
				for G in range(D,E+1):
					if A[F][G]==H:A[F][G]=0
	return A