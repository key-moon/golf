def p(g):
	A,B=sorted((A,B)for A in range(10)for B in range(10)if g[A][B]==8)[0];C=sorted((A,B,F)for A in range(10)for B in range(10)if(F:=g[A][B])%8);D=sorted(C[:2],key=lambda x:x[1]);E=sorted(C[2:],key=lambda x:x[1])
	for G in range(10):g[G]=[0]*10
	g[A][B],g[A][B+1]=D[0][2],D[1][2];g[A+1][B],g[A+1][B+1]=E[0][2],E[1][2];return g