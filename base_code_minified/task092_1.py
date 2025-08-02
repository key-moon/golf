def p(A):
	I={}
	for(B,J)in enumerate(A):
		for(C,D)in enumerate(J):
			if D:I.setdefault(D,[]).append((B,C))
	for(D,K)in I.items():
		(E,F),(G,H)=K
		for B in range(min(E,G),max(E,G)+1):
			for C in range(min(F,H),max(F,H)+1):
				if A[B][C]==0 and(B==E or B==G or C==F or C==H):A[B][C]=D
	return A