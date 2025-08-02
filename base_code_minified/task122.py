def p(g):
	B,C=next((A,B)for A in range(len(g))for B in range(len(g[0]))if g[A][B]==3 and all(g[A+C][B+D]==2 for C in(-1,0,1)for D in(-1,0,1)if C|D));A=[A for A in range(len(g[0]))if g[B][A]==3 and A!=C]
	if A:F=[A for A in A if A>C]or[max(A)];G,H=B,min(F)
	else:A=[A for A in range(len(g))if g[A][C]==3 and A!=B];F=[A for A in A if A>B]or[max(A)];G,H=min(F),C
	for D in(-1,0,1):
		for E in(-1,0,1):
			if D|E:g[B+D][C+E]=0
	for D in(-1,0,1):
		for E in(-1,0,1):
			if D|E:g[G+D][H+E]=2
	return g