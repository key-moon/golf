def p(g):
	C=len;A=range;B=[]
	for E in A(C(g[0])):
		if any(g[A][E]==5 for A in A(C(g))):B.append(E)
	D=[]
	for F in A(C(g)):
		if g[F][B[0]]==5:D.append(F)
	G,H=min(D)-1,max(D)+1;I,J=B[0],B[1];return[[g[B][A]for A in A(I,J+1)]for B in A(G,H+1)]