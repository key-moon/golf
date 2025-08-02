def p(g):
	for A in len(g)>3 and[g[A:A+3]for A in range(0,len(g),3)]or[[B[A:A+3]for B in g]for A in range(0,len(g[0]),3)]:
		if A==[A[::-1]for A in A[::-1]]:return A