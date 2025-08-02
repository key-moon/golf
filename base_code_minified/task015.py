def p(g):
	for C in range(9):
		for D in range(9):
			if g[C][D]==2:
				for(E,F)in((-1,-1),(-1,1),(1,-1),(1,1)):
					A=C+E;B=D+F
					if 0<=A<9 and 0<=B<9:g[A][B]=4
			if g[C][D]==1:
				for(E,F)in((-1,0),(1,0),(0,-1),(0,1)):
					A=C+E;B=D+F
					if 0<=A<9 and 0<=B<9:g[A][B]=7
	return g