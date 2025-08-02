def p(g):
	A=len(g)//3;D=g[A][0]
	for E in range(3):
		for F in range(3):
			if E^F&1:
				G=E*(A+1);H=F*(A+1)
				for B in range(A):
					for C in range(A):
						if g[B][C]&g[B][C]-D and not g[G+B][H+C]:g[G+B][H+C]=D
	return g