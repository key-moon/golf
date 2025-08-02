def p(g):
	C,I=len(g),len(g[0]);P=next(A for A in set(g[A][0]for A in range(C))if any(all(B==A for B in g[B])for B in range(C)));W=[A for A in range(C)if all(g[A][B]==P for B in range(I))];X=[A for A in range(I)if all(g[B][A]==P for B in range(C))];F=[];A=0
	for N in W:
		if A<N:F.append((A,N))
		A=N+1
	if A<C:F.append((A,C))
	G=[];A=0
	for O in X:
		if A<O:G.append((A,O))
		A=O+1
	if A<I:G.append((A,I))
	J,K=len(F),len(G);B=[[g[A][B]for(B,C)in G]for(A,B)in F]
	for D in range(J):
		for E in range(K):
			Q=B[D][E]
			if not Q:continue
			H=[(D-1,E),(D+1,E),(D,E-1),(D,E+1)]
			if all(0<=A<J and 0<=C<K and B[A][C]for(A,C)in H):
				R=B[H[0][0]][H[0][1]]
				if all(B[A][C]==R for(A,C)in H):Y=[(A-D,B-E)for(A,B)in H];break
		else:continue
		break
	for L in range(J):
		for M in range(K):
			if B[L][M]==Q:
				for(Z,a)in Y:
					S,T=L+Z,M+a
					if 0<=S<J and 0<=T<K:B[S][T]=R
	for(L,(b,c))in enumerate(F):
		for(M,(U,V))in enumerate(G):
			d=B[L][M]
			for e in range(b,c):g[e][U:V]=[d]*(V-U)
	return g