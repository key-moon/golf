def p(g):
	C=len(g);B=len(g[0]);A=sum(B==0 for A in g for B in A);E=[[0]*B*A for C in range(C*A)]
	for D in range(C*B-A):
		for(F,G)in enumerate(g):E[C*(D//A)+F][B*(D%A):B*(D%A)+B]=G
	return E