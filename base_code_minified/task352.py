def p(g):
	C,D=len(g),len(g[0])
	for E in range(C):
		for F in range(D):
			if g[E][F]==2:
				for G in(-1,0,1):
					for H in(-1,0,1):
						A,B=E+G,F+H
						if 0<=A<C and 0<=B<D and g[A][B]==0:g[A][B]=1
	return g