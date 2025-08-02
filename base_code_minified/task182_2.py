def p(A):
	H,E=len(A),len(A[0]);F,G,K,L=E,H,0,0
	for B in range(H):
		for C in range(E):
			if A[B][C]==5:
				if B<F:F=B
				if C<G:G=C
				if B>K:K=B
				if C>L:L=C
	S={(B-F-1,C-G-1)for B in range(F+1,K)for C in range(G+1,L)if A[B][C]not in(0,5)};T=next(iter(S));U=A[F+1+T[0]][G+1+T[1]];M=[[0]*E for A in A]
	for B in range(H):
		for C in range(E):
			P=A[B][C]
			if P and P!=5 and not M[B][C]:
				D=[(B,C)];M[B][C]=1
				for V in range(len(D)):
					W,X=D[V]
					for(Y,Z)in((1,0),(-1,0),(0,1),(0,-1)):
						I,J=W+Y,X+Z
						if 0<=I<H and 0<=J<E and not M[I][J]and A[I][J]==P:M[I][J]=1;D.append((I,J))
				a,b=D[0]
				if not(F<a<K and G<b<L):
					Q,R=H,E
					for(N,O)in D:
						if N<Q:Q=N
						if O<R:R=O
					if{(A-Q,B-R)for(A,B)in D}==S:
						for(N,O)in D:A[N][O]=U
	return A