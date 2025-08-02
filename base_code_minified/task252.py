def p(g):
	E,F=len(g),len(g[0])
	for A in range(E):
		for B in range(F):
			if g[A][B]and(A*B<1 or not g[A-1][B-1]):
				G=0;C=A;D=B
				while C<E and D<F and g[C][D]:
					if G&1:g[C][D]=4
					G+=1;C+=1;D+=1
	return g