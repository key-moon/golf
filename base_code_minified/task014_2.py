def p(g):
	B={}
	for C in g:
		for A in C:
			if A:B[A]=B.get(A,0)+1
	J=min(B,key=B.get);D,K,L=len(g),len(g),0;E,F=len(g[0]),0
	for(G,C)in enumerate(g):
		for(H,A)in enumerate(C):
			if A==J:D=min(D,G);F=max(F,G);E=min(E,H);I=max(I,H)
	return[A[E:I+1]for A in g[D:F+1]]