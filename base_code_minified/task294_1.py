def p(g):
	E,F=len(g),len(g[0])
	for A in range(E):
		for B in range(F):
			if g[A][B]==5 and(A==0 or g[A-1][B]!=5)and(B==0 or g[A][B-1]!=5):
				C=1
				while A+C<E and g[A+C][B]==5:C+=1
				D=1
				while B+D<F and g[A][B+D]==5:D+=1
				for G in range(A+1,A+C-1):
					for H in range(B+1,B+D-1):
						if g[G][H]==5:g[G][H]=2
	return g