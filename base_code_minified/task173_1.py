def p(g):
	F={}
	for G in g:
		for A in G:
			if A:F[A]=F.get(A,0)+1
	Q=min(F,key=lambda val_z:F[val_z])
	for(H,G)in enumerate(g):
		for(I,A)in enumerate(G):
			if A==Q:break
		else:continue
		break
	J={(H,I)};K=[(H,I)];L,M=len(g),len(g[0])
	while K:
		B,C=K.pop()
		for(N,O)in((1,0),(-1,0),(0,1),(0,-1)):
			D,E=B+N,C+O
			if 0<=D<L and 0<=E<M and g[D][E]and(D,E)not in J:J.add((D,E));K.append((D,E))
	P=[(A-H,B-I,g[A][B])for(A,B)in J]
	for B in range(L):
		for C in range(M):
			if all(0<=B+A<L and 0<=C+D<M and g[B+A][C+D]in(0,E)for(A,D,E)in P):
				for(N,O,R)in P:g[B+N][C+O]=R
	return g