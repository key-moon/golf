def p(A):
	B=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==2];I=min(A for(A,B)in B);L=min(A for(B,A)in B);E=max(A for(A,B)in B)-I+1;F=[[0]*E for A in range(E)]
	for(G,H)in B:F[G-I][H-L]=2
	J=next(A for B in A for A in B if A*(A-2));C=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==J];K=min(A for(A,B)in C);M=min(A for(B,A)in C);D=(E-2)//(max(A for(A,B)in C)-K+1)
	for(G,H)in C:
		for N in range(D):
			for O in range(D):F[1+(G-K)*D+N][1+(H-M)*D+O]=J
	return F