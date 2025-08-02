def p(g):
	F=next(A for B in g for A in B if A);G,H=len(g),len(g[0]);J=[(A,B)for A in range(G)for B in range(H)if g[A][B]==F];J.sort();D,E=J[0]
	if J[1][0]==D:B=[(0,1),(1,0)]
	else:B=[(1,0),(0,1)]
	A=1
	while 0<=D+B[0][0]*A<G and 0<=E+B[0][1]*A<H and g[D+B[0][0]*A][E+B[0][1]*A]==F:A+=1
	K=A;D+=B[0][0]*(A-1);E+=B[0][1]*(A-1);A=1
	while 0<=D+B[1][0]*A<G and 0<=E+B[1][1]*A<H and g[D+B[1][0]*A][E+B[1][1]*A]==F:A+=1
	L=A;C=[D,E];I=0
	while 1:
		for M in range(K if I%2==0 else L):
			C[0]+=B[I%2][0];C[1]+=B[I%2][1]
			if C[0]<0 or C[0]>=G or C[1]<0 or C[1]>=H:return g
			g[C[0]][C[1]]=F
		I+=1