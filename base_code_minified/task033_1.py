def p(g):
	C=g[0][5];D=[(A,B)for A in range(5)for B in range(5)if g[A][B]]
	for A in range(3):
		for B in range(3):
			if A!=B:
				for(E,F)in D:g[A*6+E][B*6+F]=C
	return g