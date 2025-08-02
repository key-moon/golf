def p(A):
	F={}
	for(B,M)in enumerate(A):
		for(C,J)in enumerate(M):
			if J:F.setdefault(J,[]).append((B,C))
	G={}
	for(E,H)in F.items():
		if len(H)>1:
			K,N=H[0]
			if all(A==K for(A,B)in H):G[E]='h',K
			else:G[E]='v',N
	for(E,(L,D))in G.items():
		for(B,C)in F[E]:
			if L=='v'and C!=D:I=(C>D)-(C<D);A[B][D+I]=E;A[B][C]=0
			if L=='h'and B!=D:I=(B>D)-(B<D);A[D+I][C]=E;A[B][C]=0
	return A