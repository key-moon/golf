def p(g):
	C=[(B,set(A)-{0})for(B,A)in enumerate(g)if set(A)-{0}];D=[[C[0][0]]];A=C[0][1]
	for(G,B)in C[1:]:D[-1].append(G)if B==A else D.append([G]);A=B
	H,J=len(g),len(g[0]);E=[(A,set(g[B][A]for B in range(H))-{0})for A in range(J)if set(g[B][A]for B in range(H))-{0}];F=[[E[0][0]]];A=E[0][1]
	for(I,B)in E[1:]:F[-1].append(I)if B==A else F.append([I]);A=B
	return[[next(g[A][B]for A in A for B in C if g[A][B])for C in F]for A in D]