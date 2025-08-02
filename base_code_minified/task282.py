def p(g):
	G,C=len(g),len(g[0]);D=[[0]*C for A in g]
	for(H,I)in enumerate(g):
		for(J,K)in enumerate(I):
			if K==5:
				for A in(-1,0,1):
					for B in(-1,0,1):
						E=H+A
						if 0<=E<G:
							F=J+B
							if 0<=F<C:D[E][F]=5 if A and B else 1 if A or B else 0
	return D