def p(A):
	F=set();K=len(A);L=len(A[0])
	for D in range(K):
		for E in range(L):
			if A[D][E]and(D,E)not in F:
				G=[(D,E)];H=[(D,E)];F.add((D,E))
				while H:
					I,J=H.pop()
					for(P,Q)in((1,0),(0,1),(-1,0),(0,-1)):
						C,B=I+P,J+Q
						if 0<=C<K and 0<=B<L and A[C][B]and(C,B)not in F:F.add((C,B));H+=[(C,B)];G+=[(C,B)]
				M,B=zip(*G);N,O=max(M)-min(M)+1,max(B)-min(B)+1
				if N>1 and O>1 and len(G)==2*(N+O)-4:
					for(I,J)in G:A[I][J]=3
	return A