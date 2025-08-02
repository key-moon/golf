def p(g):
	for(A,C)in enumerate(g):
		if 8 in C:B=C.index(8);break
	D=[A[B-1:B+2]for A in g[A-1:A+2]];E=[g[A-1][B],g[A+1][B],g[A][B-1],g[A][B+1]];D[1][1]=max(E,key=E.count);return D