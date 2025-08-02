def p(A):
	C,D=len(A),len(A[0]);M=[(0,A)for A in range(D)]+[(A,D-1)for A in range(1,C)]+[(C-1,A)for A in range(D-2,-1,-1)]+[(A,0)for A in range(C-2,0,-1)];G=[(B,C,A[B][C])for(B,C)in M if A[B][C]]
	for(N,O)in zip(G,G[1:]+G[:1]):
		H,I,P=N;J,K,Q=O;L=abs(H-J)+abs(I-K)
		for E in range(C):
			for F in range(D):
				B=abs(E-H)+abs(F-I)
				if B<=L and B%2==0:A[E][F]=P
				else:
					B=abs(E-J)+abs(F-K)
					if B<=L and B%2==0:A[E][F]=Q
	return A