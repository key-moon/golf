def p(A):
	B=[[0]*3 for A in[0]*3]
	for(F,G)in enumerate(A):
		for(H,I)in enumerate(G):
			if I==5:
				for C in(-1,0,1):
					for D in(-1,0,1):
						if C|D:
							try:E=A[F+C][H+D]
							except:pass
							else:
								if E and E-5:B[C+1][D+1]=E
	B[1][1]=5;return B