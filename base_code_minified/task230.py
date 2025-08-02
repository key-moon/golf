def p(g):
	for B in range(len(g)-1):
		for A in range(len(g[0])-1):
			if g[B][A:A+2]==[5,5]and g[B+1][A:A+2]==[5,5]:g[B-1][A-1],g[B-1][A+2],g[B+2][A-1],g[B+2][A+2]=1,2,3,4
	return g