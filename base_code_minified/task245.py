def p(A):
	D=len(A);F=0;E=len(A[0]);G=0
	for(B,H)in enumerate(A):
		for(C,I)in enumerate(H):
			if I==3:D=min(D,B);F=max(F,B);E=min(E,C);G=max(G,C)
	J=[A[E:G+1]for A in A[D:F+1]];K=zip(*J[::-1])
	for B in range(D,F+1):
		for C in range(E,G+1):
			if A[B][C]^3:A[B][C]=K[B-D][C-E]
	return A