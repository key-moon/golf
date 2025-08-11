def p(g):
	B=len(g[0]);C=int((B-1)/2);E=enumerate
	for(A,F)in E(g):
		if max(F)>0:
			for D in range(C):g[A][D]=g[A][0];g[A][B-D-1]=g[A][B-1]
			g[A][C]=5
	return g