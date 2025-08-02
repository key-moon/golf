def p(g):
	for A in range(len(g)-2):
		for B in range(len(g)-2):
			if sum(g[A+C][B+D]==4 for C in range(3)for D in range(3))==6:
				for C in range(3):
					for D in range(3):
						if not g[A+C][B+D]:g[A+C][B+D]=7
	return g