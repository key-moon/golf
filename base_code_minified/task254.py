def p(g):
	G,H=len(g),len(g[0]);E=[[0]*H for A in g];D=[]
	for C in range(H):
		A=0
		for B in range(G):
			if g[B][C]==5:A+=1
			elif A:D+=A,C,B-A;A=0
		if A:D+=A,C,G-A
	I=max(D)[0];J=min(D)[0]
	for(A,C,B)in D:
		if A==I:
			for F in range(B,B+A):E[F][C]=1
		elif A==J:
			for F in range(B,B+A):E[F][C]=2
	return E