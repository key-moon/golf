def p(g):
	for B in range(len(g)-6):
		for A in range(len(g[0])-6):
			C=g[B][A]
			if g[B][A:A+7]==[C]*7==g[B+6][A:A+7]and all(g[B+D][A:A+7:6]==[C,C]for D in range(7)):return[B[A:A+7]for B in g[B:B+7]]