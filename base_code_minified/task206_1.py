def p(g):
	A=[]
	for(C,F)in enumerate(g):
		for(D,B)in enumerate(F):
			if B==5:E=C,D
			elif B:A.append((C,D,B))
	G,H=min(A for(A,B,B)in A),max(A for(A,B,B)in A);I,J=min(B for(A,B,A)in A),max(B for(A,B,A)in A);K,L=(G+H)//2,(I+J)//2;M,N=E[0]-K,E[1]-L;g[E[0]][E[1]]=0
	for(C,D,B)in A:g[C+M][D+N]=B
	return g