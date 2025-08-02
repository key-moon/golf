def p(g):
	for(A,D)in enumerate(g):
		if 2 in D:break
	B=D.count(2)
	for E in range(A):
		for C in range(B+A-E):g[E][C]=3
	for F in range(1,B):
		for C in range(B-F):g[A+F][C]=1
	return g