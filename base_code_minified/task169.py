def p(g):
	E=len(g)
	for F in range(E):
		for G in range(E):
			if g[F][G]==5:
				D=[(F,G)];g[F][G]=0
				for(A,B)in D:
					for C in(1,-1):
						if 0<=A+C<E and g[A+C][B]==5:D+=[(A+C,B)];g[A+C][B]=0
						if 0<=B+C<E and g[A][B+C]==5:D+=[(A,B+C)];g[A][B+C]=0
				H=5-len(D)
				for(A,B)in D:g[A][B]=H
	return g