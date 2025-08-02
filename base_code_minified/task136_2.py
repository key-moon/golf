def p(A):
	D=len(A);F=sorted({A[B][C]for B in range(D)for C in range(D)if A[B][C]})
	for E in F:
		I=[(B,C)for B in range(D)for C in range(D)if A[B][C]==E];G,H=zip(*I);J,K=min(G),max(G);L,M=min(H),max(H)
		if E==F[0]:
			B,C=J,L
			while B and C:B-=1;C-=1;A[B][C]=E
		else:
			B,C=K,M
			while B<D-1 and C<D-1:B+=1;C+=1;A[B][C]=E
	return A