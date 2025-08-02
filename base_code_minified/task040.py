def p(g):
	D=len(g)
	for(A,B)in enumerate(g):
		for(C,E)in enumerate(B):
			if E==3:B[C]=g[(0,-1)[A>=D-1-A]][C]
	return g