def p(g):
	E=len(g);F=len(g[0])
	for A in range(E):
		for C in range(A+2,E):
			for B in range(F):
				for D in range(B+2,F):
					if all(g[A][B]==5 for B in range(B,D+1))and all(g[C][A]==5 for A in range(B,D+1))and all(g[A][B]==5 for A in range(A,C+1))and all(g[A][D]==5 for A in range(A,C+1))and all(g[A][C]==0 for A in range(A+1,C)for C in range(B+1,D)):
						for G in range(A+1,C):
							for H in range(B+1,D):g[G][H]=2
	return g