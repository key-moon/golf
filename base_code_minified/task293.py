def p(A):
	D={}
	for(B,L)in enumerate(A):
		for(C,I)in enumerate(L):
			if I:J=D.setdefault(I,(set(),set()));J[0].add(B);J[1].add(C)
	H=E=0
	for(K,(F,G))in D.items():
		if len(F)<len(G):H=K
		else:E=K
	F,G=D[H][0],D[E][1];B,C=next(iter(F)),next(iter(G));M=H if A[B][C]==E else E
	for B in F:
		for C in G:A[B][C]=M
	return A