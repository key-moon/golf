def p(g):
	J=len(g)
	for(G,H)in enumerate(g):
		for(I,K)in enumerate(H):
			if K==5:
				A=[(G,I)];g[G][I]=0
				for(E,F)in A:
					for B in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=E+B[0],F+B[1]
						if 0<=C<J and 0<=D<len(H)and g[C][D]==5:g[C][D]=0;A+=[(C,D)]
				B=2 if len(A)==6 else 1
				for(E,F)in A:g[E][F]=B
	return g