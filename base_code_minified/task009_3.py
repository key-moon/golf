def p(g):
	D=len(g)//3+1;E=len(g[0])//3+1;F=[[0]*E for A in range(D)]
	for B in range(D):
		for C in range(E):
			for G in(0,1):
				for H in(0,1):
					A=g[3*B+G][3*C+H]
					if A:F[B][C]=A
	for B in range(D):
		for C in range(E):
			A=F[B][C]
			if A:
				for I in range(E):
					if A:F[B][I]=A
				for I in range(D):
					if A:F[I][C]=A
	for B in range(D):
		for C in range(E):
			A=F[B][C]
			if A:
				for G in(0,1):
					for H in(0,1):g[3*B+G][3*C+H]=A
	return g