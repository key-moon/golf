def p(A):
	C,D=next((B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]==3 and all(A[B+D][C+E]==2 for D in(-1,0,1)for E in(-1,0,1)if D|E));B=[B for B in range(len(A[0]))if A[C][B]==3 and B!=D]
	if B:G=[A for A in B if A>D]or[max(B)];H,I=C,min(G)
	else:B=[B for B in range(len(A))if A[B][D]==3 and B!=C];G=[A for A in B if A>C]or[max(B)];H,I=min(G),D
	for E in(-1,0,1):
		for F in(-1,0,1):
			if E|F:A[C+E][D+F]=0
	for E in(-1,0,1):
		for F in(-1,0,1):
			if E|F:A[H+E][I+F]=2
	return A