def p(g):
	A=len(g)//3;B=len(g[0])//3
	for E in range(3):
		for F in range(3):
			if all(g[E*A+C][F*B+D]for C in range(A)for D in range(B)):G,H=E*A,F*B
	for C in range(len(g)):
		for D in range(len(g[0])):
			if g[C][D]==0:g[C][D]=g[G+C%A][H+D%B]
	return g