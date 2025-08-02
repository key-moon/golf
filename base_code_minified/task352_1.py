def p(g):
	for(A,E)in enumerate(g):
		for(B,F)in enumerate(E):
			if F==2:
				for C in g[max(A-1,0):A+2]:
					for D in range(max(B-1,0),B+2):
						if not C[D]:C[D]=1
	return g