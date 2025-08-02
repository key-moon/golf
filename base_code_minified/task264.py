def p(g):
	G,H=len(g),len(g[0]);A=[(A,B,C)for A in range(G-2)for B in range(H-2)for C in[tuple(g[A+C][B+D]for C in range(3)for D in range(3))]if any(C)];C={}
	for(K,B)in A:C[B]=C.get(B,0)+1
	A=[(B,D,A)for(B,D,A)in A if C[A]==1];A.sort(key=lambda x:(-x[0],-x[1]));E=[[0]*9 for A in range(9)]
	for(F,(L,M,B))in enumerate(A):
		I=F//3*3;J=F%3*3
		for D in range(9):E[I+D//3][J+D%3]=B[D]
	return E