def p(g):
	A=min(len(g),len(g[0]))if g and g[0]else 0
	def D(I):
		if A<=2:return tuple(tuple(0 if A==9 else A for A in A)for A in I)
		B=[[0 if A==9 else A for A in A]for A in I];F=list(map(list,zip(*B)));C=[[max(B[C][A],F[C][A])for A in range(A)]for C in range(A)];G=[B[2:A][::-1]for B in C[1:A]];D=[A[:]for A in C]
		for(H,J)in enumerate(G,1):
			for(K,E)in enumerate(J,2):
				if E:D[H][K]=E
		return tuple(map(tuple,D))
	B=tuple(tuple(A)for A in g)
	for E in range(256):
		C=D(B)
		if C==B:break
		B=C
	return[list(A)for A in B]
