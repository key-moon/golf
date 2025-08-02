def p(g):
	A={}
	for(B,M)in enumerate(g):
		for(C,H)in enumerate(M):
			if H:A.setdefault(H,[]).append((B,C))
	D=min(A,key=lambda v:(min(A for(A,B)in A[v]),min(A for(B,A)in A[v])));I,J=min(A for(A,B)in A[D]),min(A for(B,A)in A[D]);E=next(B for B in A if B!=D and min(A for(A,B)in A[B])==I);F=next(B for B in A if B!=D and min(A for(B,A)in A[B])==J);K=min(A for(A,B)in A[F])-I;L=min(A for(B,A)in A[E])-J;N,O=len(g),len(g[0]);P=(O-1-max(A for(B,A)in A[E]))//L
	for G in range(1,P+1):
		for(B,C)in A[E]:g[B][C+L*G]=E
	Q=(N-1-max(A for(A,B)in A[F]))//K
	for G in range(1,Q+1):
		for(B,C)in A[F]:g[B+K*G][C]=F
	return g