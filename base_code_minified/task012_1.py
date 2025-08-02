def p(g):
	I,F=len(g),len(g[0]);G=[[0]*F for A in g]
	for A in range(2,I-2):
		for B in range(2,F-2):
			H=g[A][B];C=g[A-1][B]
			if H and C and g[A+1][B]==C==g[A][B-1]==g[A][B+1]:
				for(D,E)in((2,0),(1,0),(0,1),(0,2),(-1,0),(0,-1),(0,-2),(-2,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,0)):G[A+D][B+E]=C if D*E==0 and(D or E)else H
	return G