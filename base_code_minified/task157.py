def p(g):
	A,F=len(g),len(g[0]);D=[(A,B)for A in range(A)for B in range(F)if g[A][B]==5]
	for B in range(1,A):
		if any(0<=C-B<A and g[C-B][D]==2 for(C,D)in D):break
	for(G,E)in D:
		C=G-B
		if 0<=C<A and g[C][E]==2:g[C][E]=1
	return g