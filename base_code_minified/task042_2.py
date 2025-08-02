def p(A):
	B,C=len(A),len(A[0]);M=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
	for D in range(B):
		for E in range(C):
			if A[D][E]==3:
				for(H,I)in M:
					J,K=D+H,E+I
					if 0<=J<B and 0<=K<C and A[J][K]==3:
						for L in(-1,1):
							F,G=D-H*L,E-I*L
							if 0<=F<B and 0<=G<C and A[F][G]==0:A[F][G]=8
	return A