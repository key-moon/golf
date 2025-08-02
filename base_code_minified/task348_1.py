def p(g):
	E=len(g[0])
	for C in range(E):
		A=-1
		for(B,G)in enumerate(g):
			if G[C]==7:A=B
		if A<0:continue
		for B in range(A,-1,-1):
			for D in range(A-B+1):
				for F in(C+D,C-D):
					if 0<=F<E:g[B][F]=7+(D&1)
	return g