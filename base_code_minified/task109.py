def p(A):
	for(J,G)in enumerate(A):
		if len({*G})==1 and G[0]:I=G[0];break
	K=next(B for B in range(len(A[0]))if all(A[C][B]==I for C in range(len(A))));H=[A[:K]for A in A[:J]];E=len(H);F=len(H[0]);B=[[0]*(2*F)for A in range(2*E)]
	for C in range(E):
		for D in range(F):
			if H[C][D]:B[C][D]=B[C][2*F-1-D]=B[2*E-1-C][D]=B[2*E-1-C][2*F-1-D]=I
	return B