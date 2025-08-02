def p(g):
	A,B=len(g),len(g[0]);L=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
	for C in range(A):
		for D in range(B):
			if g[C][D]==3:
				for(G,H)in L:
					I,J=C+G,D+H
					if 0<=I<A and 0<=J<B and g[I][J]==3:
						for K in(-1,1):
							E,F=C-G*K,D-H*K
							if 0<=E<A and 0<=F<B and g[E][F]==0:g[E][F]=8
	return g