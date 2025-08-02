def p(g):
	J=sum(g,[]);K=set(J)-{0};B=min(K,key=J.count);L=(K-{B}).pop();D,E=len(g),len(g[0]);C=[(A,C)for A in range(D)for C in range(E)if g[A][C]==B and(A<1 or A>D-2 or C<1 or C>E-2)]
	while C:
		F,A=C.pop()
		if g[F][A]==B:
			g[F][A]=0
			for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
				G,H=F+M,A+N
				if 0<=G<D and 0<=H<E and g[G][H]==B:C.append((G,H))
	for I in g:
		for A in range(len(I)):
			if I[A]==B:I[A]=L
	return g