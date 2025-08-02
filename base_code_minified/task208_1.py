def p(g):
	E,F=len(g),len(g[0]);A={}
	for C in g:
		for B in C:A[B]=A.get(B,0)+1
	D=min(A,key=A.get)
	for(G,C)in enumerate(g):
		for(H,B)in enumerate(C):
			if B==D:g[E-1-G][F-1-H]=D
	return g