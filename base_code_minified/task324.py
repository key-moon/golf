def p(A):
	D,E=len(A),len(A[0]);G=max({B for A in A for B in A},key=lambda G:sum(A.count(G)for A in A));J=[(B,C,A[B][C])for B in range(D)for C in range(E)if A[B][C]!=G and sum(0<=B+F<D and 0<=C+G<E and A[B+F][C+G]==A[B][C]for(F,G)in((1,0),(-1,0),(0,1),(0,-1)))<2]
	for B in range(D):
		for C in range(E):
			if A[B][C]==G:
				H=10**9;F=None
				for(K,L,M)in J:
					I=abs(B-K)
					if I==abs(C-L)<H:H=I;F=M
				if F is not None:A[B][C]=F
	return A