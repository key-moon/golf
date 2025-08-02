def p(g):
	I,J=len(g),len(g[0]);D=[(A,B)for A in range(I)for B in range(J)if g[A][B]==5];E,F=min(A for(A,B)in D),max(A for(A,B)in D);G,H=min(A for(B,A)in D),max(A for(B,A)in D);C=[[0]*J for A in range(I)]
	for A in range(E,F+1):
		for B in range(G,H+1):C[A][B]=5
	L=F-E>H-G
	for A in range(I):
		for B in range(J):
			K=g[A][B]
			if K and K!=5:
				if L:
					if A<E:C[E-1][B]=5
					if A>F:C[F+1][B]=5
				else:
					if B<G:C[A][G-1]=5
					if B>H:C[A][H+1]=5
	return C