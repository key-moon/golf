def p(A):
	E,F=len(A),len(A[0]);B=[(B,C)for B in range(E)for C in range(F)if A[B][C]==2];G,H=min(A for(A,B)in B),min(A for(B,A)in B);I=[(A-G,B-H)for(A,B)in B]
	for(J,K)in B:A[J][K]=0
	for C in range(E):
		for D in range(F):
			if(C,D)!=(G,H)and all(0<=C+B<E and 0<=D+G<F and A[C+B][D+G]==0 for(B,G)in I):
				for(L,M)in I:A[C+L][D+M]=2
				return A
	return A