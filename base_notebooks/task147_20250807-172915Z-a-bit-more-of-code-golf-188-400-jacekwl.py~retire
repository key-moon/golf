def p(g):
	C=[A[:]for A in g];D,E=len(g),len(g[0])
	for A in range(D):
		for B in range(E):
			if g[A][B]==3:
				for(F,G)in[(0,1),(1,0),(0,-1),(-1,0)]:
					if 0<=A+F<D and 0<=B+G<E and g[A+F][B+G]==3:C[A][B]=8;break
	return C