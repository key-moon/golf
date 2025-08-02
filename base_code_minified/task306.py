def p(A):
	F,G=len(A),len(A[0]);L=[B for B in range(F)if A[B][0]and A[B]==[A[B][0]]*G];M=[B for B in range(G)if A[0][B]and all(A[C][B]==A[0][B]for C in range(F))];H=[-1]+L+[F];I=[-1]+M+[G];J=[(H[A]+1,H[A+1],I[B]+1,I[B+1])for A in range(len(H)-1)for B in range(len(I)-1)]
	for(B,C,D,E)in J:
		if any(A[B][C]for B in range(B,C)for C in range(D,E)):N=[A[D:E]for A in A[B:C]];O=B,C,D,E;break
	for(B,C,D,E)in J:
		if(B,C,D,E)!=O:
			for K in range(B,C):A[K][D:E]=N[K-B]
	return A