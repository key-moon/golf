def p(A):
	R,N=len(A),len(A[0]);E=[B for(B,A)in enumerate(A)if A.count(A[0])==N];O=A[E[0]][0];G=[B for B in range(N)if A[E[0]][B]==O];H,I=len(E)-1,len(G)-1;F=[[A[E[B]+1][G[C]+1]for C in range(I)]for B in range(H)]
	for D in{B for A in F for B in A}-{0}:
		for B in range(H):
			J=[A for A in range(I)if F[B][A]==D]
			if len(J)>1:
				K,L=min(J),max(J)
				for C in range(K+1,L):F[B][C]=D
		for C in range(I):
			M=[A for A in range(H)if F[A][C]==D]
			if len(M)>1:
				K,L=min(M),max(M)
				for B in range(K+1,L):F[B][C]=D
	for B in range(H):
		for C in range(I):
			D=F[B][C]
			if D:
				for P in range(E[B]+1,E[B+1]):
					for Q in range(G[C]+1,G[C+1]):A[P][Q]=D
	return A