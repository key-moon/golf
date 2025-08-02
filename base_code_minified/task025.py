def p(A):
	I,J=len(A),len(A[0]);K={}
	for B in range(I):
		for C in range(J):
			E=A[B][C]
			if E:K.setdefault(E,[]).append((B,C))
	F=[[0]*J for A in range(I)]
	for(E,D)in K.items():
		G=max({A for(A,B)in D},key=lambda L:sum(A==L for(A,B)in D));L=sum(A==G for(A,B)in D);H=max({A for(B,A)in D},key=lambda O:sum(A==O for(B,A)in D));M=sum(A==H for(B,A)in D)
		if L+M>2:
			if M>L:
				for(B,C)in D:
					if C==H:F[B][C]=E
					else:F[B][H+(C>H and 1 or-1)]=E
			else:
				for(B,C)in D:
					if B==G:F[B][C]=E
					else:F[G+(B>G and 1 or-1)][C]=E
	return F