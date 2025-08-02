def p(A):
	C,D={},set()
	for(E,F)in enumerate(A):
		for(G,B)in enumerate(F):
			if B&1:C[E]=B
			elif B:D|={G}
	return[[C.get(B)or(A in D)*2 for(A,E)in enumerate(A[0])]for(B,E)in enumerate(A)]