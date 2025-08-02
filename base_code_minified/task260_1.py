def p(g):
	A=len(g);E=[[0]*A for B in range(A)];B=[(B,C)for B in range(A)for C in range(A)if g[B][C]and g[B][C]!=5];F=g[B[0][0]][B[0][1]];C,D=next((A,B)for(A,B)in B if 5 in g[A]);H=1 if g[C].index(5)>D else-1;I=max(A.count(5)for A in g)+2
	for(C,D)in B:E[C][D]=F;G=D+H*I;0<=G<A and E[C].__setitem__(G,F)
	return E