def p(A):
	E=next(A for B in A for A in B if A and A!=4);F=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==E];L=min(A for(A,B)in F);M=max(A for(A,B)in F);N=min(A for(B,A)in F);O=max(A for(B,A)in F);G,H=len(A),len(A[0]);D=[A[:]for A in A]
	for B in range(N,O+1):
		if not D[L][B]:D[L][B]=E
		if not D[M][B]:D[M][B]=E
	for C in range(L,M+1):
		if not D[C][N]:D[C][N]=E
		if not D[C][O]:D[C][O]=E
	I=set();P=[(A,B)for A in(0,G-1)for B in range(H)if not D[A][B]]+[(B,A)for A in(0,H-1)for B in range(G)if not D[B][A]]
	for(C,B)in P:
		if(C,B)in I:continue
		I.add((C,B))
		for(Q,R)in((1,0),(-1,0),(0,1),(0,-1)):
			J,K=C+Q,B+R
			if 0<=J<G and 0<=K<H and(J,K)not in I and not D[J][K]:P.append((J,K))
	for C in range(G):
		for B in range(H):
			if A[C][B]==0 and(C,B)not in I:A[C][B]=4
	return A