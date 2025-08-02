def p(g):
	H,I=len(g),len(g[0]);E,J={},{}
	for B in range(H):
		for C in range(I):
			A=g[B][C]
			if A and A not in E:
				D=[]
				for(F,G)in((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
					K,L=B+F,C+G
					if 0<=K<H and 0<=L<I and g[K][L]:D.append((F,G))
				if len(D)>1:E[A]=D;J[A]=g[B+D[0][0]][C+D[0][1]]
	for B in range(H):
		for C in range(I):
			A=g[B][C]
			if A in E:
				for(F,G)in E[A]:g[B+F][C+G]=J[A]
	return g