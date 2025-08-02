def p(g):
	H,I=len(g),len(g[0]);E=min(A for A in range(H)for B in range(I)if g[A][B]==5);F=max(A for A in range(H)for B in range(I)if g[A][B]==5);G=min(A for B in range(H)for A in range(I)if g[B][A]==5);J=max(A for B in range(H)for A in range(I)if g[B][A]==5)
	for B in range(G,J+1):
		if g[E][B]==0:C,D=E,B;break
	else:
		for B in range(G,J+1):
			if g[F][B]==0:C,D=F,B;break
		else:
			for A in range(E,F+1):
				if g[A][G]==0:C,D=A,G;break
			else:
				for A in range(E,F+1):
					if g[A][J]==0:C,D=A,J;break
	for A in range(E+1,F):
		for K in range(G+1,J):
			if g[A][K]==0:g[A][K]=8
	if C==E:
		for A in range(C+1):g[A][D]=8
	elif C==F:
		for A in range(C,H):g[A][D]=8
	elif D==G:
		for B in range(D+1):g[C][B]=8
	else:
		for B in range(D,I):g[C][B]=8
	return g