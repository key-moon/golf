def p(A):
	M,I=len(A),len(A[0]);J=[[0]*I for A in A]
	for K in range(M):
		for L in range(I):
			if A[K][L]==0 and not J[K][L]:
				B=[(K,L)];J[K][L]=1
				for Q in range(len(B)):
					N,O=B[Q]
					for(R,S)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=N+R,O+S
						if 0<=C<M and 0<=D<I and A[C][D]==0 and not J[C][D]:J[C][D]=1;B.append((C,D))
				E=min(A for(A,B)in B);F=max(A for(A,B)in B);G=min(A for(B,A)in B);H=max(A for(B,A)in B);P=F-E
				if P==H-G and len(B)==(P+1)**2 and E and G and F<M-1 and H<I-1 and all(A[B][G-1]==5 for B in range(E,F+1))and all(A[B][H+1]==5 for B in range(E,F+1))and all(A[E-1][B]==5 for B in range(G,H+1))and all(A[F+1][B]==5 for B in range(G,H+1)):
					for(N,O)in B:A[N][O]=2
	return A