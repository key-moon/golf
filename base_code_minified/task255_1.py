def p(A):
	F=len(A);G=len(A[0]);H={}
	for L in A:
		for K in L:H[K]=H.get(K,0)+1
	D=max(H,key=H.get);E=[]
	for B in range(F):
		for C in(0,G-1):
			if A[B][C]==D:E.append((B,C))
	for C in range(G):
		for B in(0,F-1):
			if A[B][C]==D:E.append((B,C))
	while E:
		B,C=E.pop()
		if A[B][C]==D:
			A[B][C]=-1
			for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
				I,J=B+M,C+N
				if 0<=I<F and 0<=J<G and A[I][J]==D:E.append((I,J))
	for B in range(F):
		for C in range(G):
			if A[B][C]==D:A[B][C]=3
			elif A[B][C]==-1:A[B][C]=D
	return A