def p(A):
	G,H={},{}
	for(B,I)in enumerate(A):
		for(C,D)in enumerate(I):
			if D:G.setdefault(B,[]).append(C);H.setdefault(C,[]).append(B)
	for(B,E)in G.items():
		if len(E)==2:
			D,F=sorted(E)
			for C in range(D,F+1):A[B][C]=8
	for(C,E)in H.items():
		if len(E)==2:
			D,F=sorted(E)
			for B in range(D,F+1):A[B][C]=8
	return A