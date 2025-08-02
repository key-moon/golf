def p(g):
	M=len(g);B=M//3;A=B+1;K=g[B][B];G=[[any(g[C*A+E][D*A+F]for E in range(B)for F in range(B))for D in range(3)]for C in range(3)]
	for E in range(3):
		for F in range(3):
			if not G[E][F]:
				H=[A for A in range(3)if G[E][A]]
				if len(H)>1:
					I,J=H[0],H[1]
					for C in range(B):
						for D in range(B):
							if g[E*A+C][I*A+D]or g[E*A+C][J*A+D]:g[E*A+C][F*A+D]=K
				else:
					L=[A for A in range(3)if G[A][F]];I,J=L[0],L[1]
					for C in range(B):
						for D in range(B):
							if g[I*A+C][F*A+D]or g[J*A+C][F*A+D]:g[E*A+C][F*A+D]=K
	return g