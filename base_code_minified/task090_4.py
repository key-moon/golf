def p(g):
	F=len(g);H=len(g[0]);G=0
	for A in range(F):
		for C in range(A,F):
			B=0
			for E in range(H):
				if all(g[A][E]==0 for A in range(A,C+1)):
					B+=1
					if B*(C-A+1)>G:G=B*(C-A+1);D=A,C,E-B+1,E
				else:B=0
	for I in range(D[0],D[1]+1):
		for J in range(D[2],D[3]+1):g[I][J]=6
	return g