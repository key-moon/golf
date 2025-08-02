def p(g):
	B,C=len(g),len(g[0]);L=[(0,A)for A in range(C)]+[(A,C-1)for A in range(1,B)]+[(B-1,A)for A in range(C-2,-1,-1)]+[(A,0)for A in range(B-2,0,-1)];F=[(A,B,g[A][B])for(A,B)in L if g[A][B]]
	for(M,N)in zip(F,F[1:]+F[:1]):
		G,H,O=M;I,J,P=N;K=abs(G-I)+abs(H-J)
		for D in range(B):
			for E in range(C):
				A=abs(D-G)+abs(E-H)
				if A<=K and A%2==0:g[D][E]=O
				else:
					A=abs(D-I)+abs(E-J)
					if A<=K and A%2==0:g[D][E]=P
	return g