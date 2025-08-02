def p(A):
	D={}
	for(E,N)in enumerate(A):
		for(O,I)in enumerate(N):
			if I:D.setdefault(I,[]).append((E,O))
	B=next(A for(A,B)in D.items()if len(B)==4);J,K=zip(*D[B]);F,L=set(J),set(K);M,G=len(A),len(A[0]);C=[[0]*G for A in range(M)]
	if len(F)==2:
		for H in F:C[H]=[B]*G
	else:H=max(F,key=J.count);C[H]=[B]*G
	if len(L)>2:
		P=max(L,key=K.count)
		for E in range(M):C[E][P]=B
	return C