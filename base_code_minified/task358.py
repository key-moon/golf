def p(g):
	B,E=len(g),len(g[0])
	for A in range(B):
		C=[B for B in range(E)if g[A][B]]
		if len(C)>1:
			F=C[0];G=len(C);K=[g[A][F+B]for B in range(G)];D=next(C for C in C if A and g[A-1][C]or A+1<B and g[A+1][C]);H=[g[A][D]for A in range(B)if g[A][D]];L=min(A for A in range(B)if g[A][D])
			for I in range(B):g[I][D]=H[(I-L)%len(H)]
			for J in range(E):g[A][J]=K[(J-F)%G]
			break
	return g