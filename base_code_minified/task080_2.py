def p(A):
	D,J=len(A),len(A[0]);Q=next(B for B in set(A[B][0]for B in range(D))if any(all(A==B for A in A[C])for C in range(D)));X=[B for B in range(D)if all(A[B][C]==Q for C in range(J))];Y=[B for B in range(J)if all(A[C][B]==Q for C in range(D))];G=[];B=0
	for O in X:
		if B<O:G.append((B,O))
		B=O+1
	if B<D:G.append((B,D))
	H=[];B=0
	for P in Y:
		if B<P:H.append((B,P))
		B=P+1
	if B<J:H.append((B,J))
	K,L=len(G),len(H);C=[[A[B][C]for(C,D)in H]for(B,C)in G]
	for E in range(K):
		for F in range(L):
			R=C[E][F]
			if not R:continue
			I=[(E-1,F),(E+1,F),(E,F-1),(E,F+1)]
			if all(0<=A<K and 0<=B<L and C[A][B]for(A,B)in I):
				S=C[I[0][0]][I[0][1]]
				if all(C[A][B]==S for(A,B)in I):Z=[(A-E,B-F)for(A,B)in I];break
		else:continue
		break
	for M in range(K):
		for N in range(L):
			if C[M][N]==R:
				for(a,b)in Z:
					T,U=M+a,N+b
					if 0<=T<K and 0<=U<L:C[T][U]=S
	for(M,(c,d))in enumerate(G):
		for(N,(V,W))in enumerate(H):
			e=C[M][N]
			for f in range(c,d):A[f][V:W]=[e]*(W-V)
	return A