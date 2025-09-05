def p(g,R=range):
	C=len(g);I=1;F,G=0,0;H=[0,5];J,K=0,0
	for A in R(C):
		for B in R(C):
			if g[A][B]not in H and I:
				I=0;J,K=A,B;D=A;E=B
				while D<C and g[D][B]not in H:D+=1
				while E<C and g[A][E]not in H:E+=1
				F=D-A;G=E-B
	for A in R(C-F+1):
		for B in R(C-G+1):
			if g[A][B]==5:
				for L in R(F):
					for M in R(G):g[A+L][B+M]=g[J+L][K+M]
	return g