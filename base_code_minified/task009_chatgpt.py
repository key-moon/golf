def p(A):
	J,R=len(A),len(A[0]);K=max(set(A for B in A for A in B if A),key=lambda F:sum(A.count(F)for A in A));D=[-1]+[B for B in range(J)if all(A==K for A in A[B])]+[J];E=[-1]+[B for B in range(R)if all(A[C][B]==K for C in range(J))]+[R];G=[[0]*(len(E)-1)for A in range(len(D)-1)]
	for F in range(len(D)-1):
		for B in range(len(E)-1):
			for L in range(D[F]+1,D[F+1]):
				for M in range(E[B]+1,E[B+1]):
					N=A[L][M]
					if N and N!=K:G[F][B]=N
	for H in G:
		for C in set(H):
			if C:
				O=min(A for(A,B)in enumerate(H)if B==C);P=max(A for(A,B)in enumerate(H)if B==C)
				for I in range(O,P+1):
					if H[I]==0:H[I]=C
	for B in range(len(E)-1):
		Q=[G[A][B]for A in range(len(D)-1)]
		for C in set(Q):
			if C:
				O=min(A for(A,B)in enumerate(Q)if B==C);P=max(A for(A,B)in enumerate(Q)if B==C)
				for I in range(O,P+1):
					if G[I][B]==0:G[I][B]=C
	for F in range(len(D)-1):
		for B in range(len(E)-1):
			if G[F][B]:
				for L in range(D[F]+1,D[F+1]):
					for M in range(E[B]+1,E[B+1]):A[L][M]=G[F][B]
	return A