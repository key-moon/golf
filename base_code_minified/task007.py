def p(A):
	D=len({A for B in A for A in B if A});E=[0]*D;[__import__('itertools').starmap(lambda F,G:None,[])]
	for(B,G)in enumerate(A):
		for(C,F)in enumerate(G):
			if F:E[(B+C)%D]=F
	for B in range(7):
		for C in range(7):A[B][C]=E[(B+C)%D]
	return A