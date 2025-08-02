def p(g):
	H,I=len(g),len(g[0]);A=min(H,I);C=A*A;F=[[0]*C for A in[0]*C]
	for D in range(A):
		for E in range(A):
			G=g[D][E]
			if G:
				J=D*A+A//2;K=E*A+A//2
				for B in range(C):
					if B//A==D or B%A==E:F[B//A*A+A//2][B%A*A+A//2]=G
	return F