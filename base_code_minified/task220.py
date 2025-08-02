def p(A,B={2:1,3:6,8:4}):
	G,H=len(A),len(A[0])
	for C in range(G):
		for D in range(H):
			I=A[C][D]
			if I:
				J=B[I]
				for E in(-1,0,1):
					for F in(-1,0,1):
						if E|F and 0<=C+E<G and 0<=D+F<H:A[C+E][D+F]=J
	return A