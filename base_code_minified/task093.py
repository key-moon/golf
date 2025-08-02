def p(g):
	K,J=len(g),len(g[0]);E=K;F=-1;C=J;D=-1
	for(A,H)in enumerate(g):
		for(B,I)in enumerate(H):
			if I==5:
				if A<E:E=A
				if A>F:F=A
				if B<C:C=B
				if B>D:D=B
	G=[[0]*J for A in g]
	for A in range(E,F+1):G[A][C:D+1]=[5]*(D-C+1)
	if F-E>D-C:
		for(A,H)in enumerate(g):
			for(B,I)in enumerate(H):
				if I%5:
					if B<C:G[A][C-1]=5
					if B>D:G[A][D+1]=5
	else:
		for(A,H)in enumerate(g):
			for(B,I)in enumerate(H):
				if I%5:
					if A<E:G[E-1][B]=5
					if A>F:G[F+1][B]=5
	return G