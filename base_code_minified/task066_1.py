def p(A):
	G,H=len(A),len(A[0]);I=[(B,C)for B in range(G)for C in range(H)if A[B][C]==3];N={(B,C)for B in range(G)for C in range(H)if A[B][C]==2};J=I[:];K=set(I);L={};F=1,0,-1,0,0,1,0,-1
	while J:
		B,C=J.pop(0)
		if any((B+F[A],C+F[A+1])in N for A in(0,2,4,6)):break
		for M in(0,2,4,6):
			D,E=B+F[M],C+F[M+1]
			if 0<=D<G and 0<=E<H and(D,E)not in K and A[D][E]==0:K.add((D,E));L[D,E]=B,C;J.append((D,E))
	while(B,C)not in I:A[B][C]=3;B,C=L[B,C]
	return A