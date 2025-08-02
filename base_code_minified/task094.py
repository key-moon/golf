def p(g):
	F,E=len(g),len(g[0])
	for B in range(F):
		for A in range(E):
			if g[B][A]==1 and(B<1 or g[B-1][A]!=1)and(A<1 or g[B][A-1]!=1):
				C=1
				while A+C<E and g[B][A+C]==1:C+=1
				G=B+C//2;H=A+C//2
				for D in range(F):
					if g[D][H]==8:g[D][H]=6
				for D in range(E):
					if g[G][D]==8:g[G][D]=6
	return g