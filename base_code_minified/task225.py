def p(g):
	for G in range(5):
		for H in range(5):
			if g[G][H]and g[G][H+1]and g[G+1][H]and g[G+1][H+1]:C,D=G,H;break
		else:continue
		break
	I=g[C][D];J=g[C][D+1];K=g[C+1][D];L=g[C+1][D+1]
	for(E,F)in((0,0),(0,1),(1,0),(1,1)):
		A,B=C-1-E,D-1-F
		if 0<=A<6 and 0<=B<6 and g[A][B]==0:g[A][B]=L
	for(E,F)in((0,0),(0,1),(1,0),(1,1)):
		A,B=C-1-E,D+2+F
		if 0<=A<6 and 0<=B<6 and g[A][B]==0:g[A][B]=K
	for(E,F)in((0,0),(0,1),(1,0),(1,1)):
		A,B=C+2+E,D-1-F
		if 0<=A<6 and 0<=B<6 and g[A][B]==0:g[A][B]=J
	for(E,F)in((0,0),(0,1),(1,0),(1,1)):
		A,B=C+2+E,D+2+F
		if 0<=A<6 and 0<=B<6 and g[A][B]==0:g[A][B]=I
	return g