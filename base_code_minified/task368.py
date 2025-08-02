def p(g):
	L,J=len(g),len(g[0]);F=[[0]*J for A in g];M={}
	for G in range(L):
		for H in range(J):
			if g[G][H]and not F[G][H]:
				K=[(G,H)];F[G][H]=1;A=[]
				while K:
					N,O=K.pop();A.append((N,O))
					for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=N+T,O+U
						if 0<=D<L and 0<=E<J and g[D][E]and not F[D][E]:F[D][E]=1;K.append((D,E))
				B=min(A for(A,B)in A);C=min(A for(B,A)in A);P=tuple(sorted((A-B,D-C)for(A,D)in A));M.setdefault(P,[]).append((B,C,A))
	for(P,Q)in M.items():
		for(B,C,A)in Q:
			if len({g[A][B]for(A,B)in A})>1:I=B,C,A;break
		V={(A-I[0],B-I[1]):g[A][B]for(A,B)in I[2]}
		for(B,C,A)in Q:
			if A!=I[2]:
				for(R,S)in A:g[R][S]=V[R-B,S-C]
	return g