def p(A):
	I,J=len(A),len(A[0]);H={};N={A for B in A for A in B if A not in(0,5)}
	for F in N:
		G=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==F];O=min(A for(A,B)in G);P=min(A for(B,A)in G);Q=tuple(sorted((A-O,B-P)for(A,B)in G));H[Q]=F
		for(B,C)in G:A[B][C]=0
	for B in range(I):
		for C in range(J):
			if A[B][C]==5 and(B==0 or A[B-1][C]!=5)and(C==0 or A[B][C-1]!=5):
				D=1
				while C+D<J and A[B][C+D]==5:D+=1
				E=1
				while B+E<I and all(A[B+E][C+D]==5 for D in range(D)):E+=1
				K=tuple(sorted((E-B,F-C)for E in range(B,B+E)for F in range(C,C+D)if A[E][F]!=5))
				if K in H:
					F=H[K]
					for L in range(B,B+E):
						for M in range(C,C+D):
							if A[L][M]!=5:A[L][M]=F
	return A