def p(g):
	E=[[0]*len(g[0])for A in g]
	for A in range(2,len(g)-2):
		for B in range(2,len(g[0])-2):
			F=g[A][B];G=g[A-1][B]
			if F*G*g[A+1][B]*g[A][B-1]*g[A][B+1]:
				for C in range(-2,3):
					for D in range(-2,3):E[A+C][B+D]=G if not C*D and abs(C)+abs(D)>0 else F
	return E