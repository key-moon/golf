def p(g):
	C=len(g);D=len(g[0])
	for B in range(C-2):
		for A in range(D-2):
			if all(g[B+C][A+D]==0 for C in range(3)for D in range(3)):
				for E in range(3):g[B+E][A:A+3]=[1]*3
				return g
	return g