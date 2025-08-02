def p(g):
	D=E=C=0;F=len(g)-4
	for B in range(F):
		for A in range(F):
			G=len({*g[B][A:A+5],*g[B+1][A:A+5],*g[B+2][A:A+5],*g[B+3][A:A+5],*g[B+4][A:A+5]})
			if G>D:D,E,C=G,B,A
	return[g[E+A][C:C+5][::-1]for A in range(5)]