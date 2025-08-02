def p(g):
	C,D=len(g),len(g[0]);E={}
	for A in range(C):
		for B in range(D):
			K=g[A][B]
			if K:E[K]=E.get(K,0)+1
	F=min(E,key=E.get);G,H=C,D;L,M=-1,-1
	for A in range(C):
		for B in range(D):
			if g[A][B]==F:
				if A<G:G=A
				if A>L:L=A
				if B<H:H=B
				if B>M:M=B
	for N in(G,L):
		for O in(H,M):
			I=-1 if N==G else 1;J=-1 if O==H else 1;A,B=N+I,O+J
			while 0<=A<C and 0<=B<D and g[A][B]in(0,F):A+=I;B+=J
			if 0<=A<C and 0<=B<D and g[A][B]not in(0,F):
				A+=I;B+=J
				while 0<=A<C and 0<=B<D:
					if g[A][B]==0:g[A][B]=F
					A+=I;B+=J
	return g