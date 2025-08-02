def p(g):
	for(D,A)in enumerate(g):
		if 3 in A:B=D;C=A.index(3)
		if 4 in A:E=D;F=A.index(4)
	g[B][C]=0;g[B+(E>B)-(E<B)][C+(F>C)-(F<C)]=3;return g