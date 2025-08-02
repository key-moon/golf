def p(g):
	for(A,E)in enumerate(g):
		for(B,F)in enumerate(E):
			if F==5:
				for C in(1,0,-1):
					for D in(1,0,-1):
						try:g[A+C][B+D]=g[A+C][B+D]or 1
						except:0
	return g