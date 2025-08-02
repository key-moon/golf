def p(g):
	G=len(g);H=len(g[0])
	for B in range(G):
		A=0
		while A<H:
			if g[B][A]==5:
				C=A
				while C<H and g[B][C]==5:C+=1
				if C-A>2:I,J,O=B,A,C-1;break
				A=C
			else:A+=1
		else:continue
		break
	Q=max(A for A in range(I,G)if all(g[A][B]==5 for B in range(J,O+1)));K=[(A-(I+1),B-(J+1))for A in range(I+1,Q)for B in range(J+1,O)if g[A][B]]
	if not K:return g
	R=g[I+1+K[0][0]][J+1+K[0][1]];L=set()
	for B in range(G):
		for A in range(H):
			if g[B][A]==1 and(B,A)not in L:
				P=[(B,A)];L.add((B,A));F=[(B,A)]
				for(M,N)in P:
					for(S,T)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=M+S,N+T
						if 0<=D<G and 0<=E<H and g[D][E]==1 and(D,E)not in L:L.add((D,E));P.append((D,E));F.append((D,E))
				U,V=min(A for(A,B)in F),min(A for(B,A)in F)
				if sorted((A-U,B-V)for(A,B)in F)==sorted(K):
					for(M,N)in F:g[M][N]=R
	return g