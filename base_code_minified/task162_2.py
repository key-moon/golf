def p(g):
	for A in range(len(g)-2):
		for B in range(len(g[0])-2):
			if not any(g[A+C][B+D]for C in(0,1,2)for D in(0,1,2)):
				for C in(0,1,2):
					for D in(0,1,2):g[A+C][B+D]=1
				return g