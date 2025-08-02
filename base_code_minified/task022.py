def p(g):
	A=[[0]*3 for A in[0]*3]
	for(E,F)in enumerate(g):
		for(G,H)in enumerate(F):
			if H==5:
				for B in(-1,0,1):
					for C in(-1,0,1):
						if B|C:
							try:D=g[E+B][G+C]
							except:pass
							else:
								if D and D-5:A[B+1][C+1]=D
	A[1][1]=5;return A