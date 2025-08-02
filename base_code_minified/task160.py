def p(g):
	C=[A[:]for A in g]
	for B in range(len(g)-2):
		for A in range(len(g[0])-2):
			if g[B][A:A+3]==[1,1,1]and g[B+1][A:A+3]==[1,0,1]and g[B+2][A:A+3]==[1,1,1]:
				for(D,E)in((0,1),(1,0),(1,1),(1,2),(2,1)):C[B+D][A+E]=2
				for(D,E)in((0,0),(0,2),(2,0),(2,2)):C[B+D][A+E]=0
	return C