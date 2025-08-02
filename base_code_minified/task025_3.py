def p(A):
	J,K=len(A),len(A[0]);D={}
	for E in range(J):
		B=A[E][0]
		if B and A[E].count(B)==K:D.setdefault(B,[]).append((1,E))
	for F in range(K):
		B=A[0][F]
		if B and all(A[C][F]==B for C in range(J)):D.setdefault(B,[]).append((0,F))
	for(G,M)in enumerate(A):
		for(H,I)in enumerate(M):
			for(L,C)in D.get(I,()):
				if L and G!=C:A[C+(1 if G>C else-1)][H]=I
				if not L and H!=C:A[G][C+(1 if H>C else-1)]=I
	return A