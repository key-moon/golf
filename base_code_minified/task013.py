def p(A):
	J=[(B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A];(E,F,G),(H,K,I)=J
	if E*H:
		B=H-E
		for(L,C)in enumerate(A):
			for D in range(len(C)):C[D]=G if(L-E)%(B*2)<B else I
	else:
		B=K-F
		for C in A:
			for D in range(len(C)):C[D]=G if(D-F)%(B*2)<B else I
	return A