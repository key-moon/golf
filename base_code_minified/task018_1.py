def p(g):
	F,G=len(g),len(g[0]);H=[A[:]for A in g];I=[[0]*G for A in range(F)];X=[(1,0),(-1,0),(0,1),(0,-1)];J=[]
	for K in range(F):
		for L in range(G):
			if g[K][L]and not I[K][L]:
				C=[(K,L)];I[K][L]=1
				for(Y,Z)in C:
					for(N,O)in X:
						D,E=Y+N,Z+O
						if 0<=D<F and 0<=E<G and g[D][E]and not I[D][E]:I[D][E]=1;C.append((D,E))
				R,S=C[0];a=tuple(sorted((A-R,B-S,g[A][B])for(A,B)in C));J.append((a,C,R,S))
	P={}
	for(A,Q,B,B)in J:P[A]=P.get(A,0)+1
	for(A,Q,B,B)in J:
		if P[A]==2:M=A;b=[B for B in J if B[0]==A];break
	for(B,Q,B,B)in b:
		for(c,d)in Q:H[c][d]=0
	T=[A for(A,B,C)in M];U=[A for(B,A,C)in M];e=max(T)-min(T)+1;f=max(U)-min(U)+1
	for V in range(F-e+1):
		for W in range(G-f+1):
			if all(H[V+A][W+B]==0 for(A,B,C)in M):
				for(N,O,h)in M:H[V+N][W+O]=h
				return H