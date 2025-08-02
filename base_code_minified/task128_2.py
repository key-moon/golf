def p(g):
	H,I=len(g),len(g[0]);C=[H]*5;D=[-1]*5
	for(B,E)in enumerate(g):
		for(F,A)in enumerate(E):
			if A:
				if B<C[A]:C[A]=B
				if B>D[A]:D[A]=B
	G=[[0]*I for A in g]
	for(B,E)in enumerate(g):
		for(F,A)in enumerate(E):
			if A:G[B-(D[A]-C[A]+1)][F]=A
	return G