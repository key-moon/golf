def p(g):
	for(C,D)in enumerate(g):
		if 2 in D:E,A=D.index(2),C
		if 3 in D:B,F=D.index(3),C
	if E>B:E,B=B,E
	if A>F:A,F=F,A
	for G in range(E,B+1):
		if g[A][G]<1:g[A][G]=8
	for C in range(A,F+1):
		if g[C][B]<1:g[C][B]=8
	return g