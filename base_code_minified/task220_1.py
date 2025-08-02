def p(A):
	B={3:6,8:4,2:1}
	for(F,G)in enumerate(A):
		for(H,C)in enumerate(G):
			if C in B:
				for D in(-1,0,1):
					for E in(-1,0,1):
						if D or E:A[F+D][H+E]=B[C]
	return A