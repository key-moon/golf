def p(g):
	H=[(A,B)for A in range(len(g))for B in range(len(g[0]))if g[A][B]];I,J=max(((A,B)for A in H for B in H if g[A[0]][A[1]]!=g[B[0]][B[1]]),key=lambda x:abs(x[0][0]-x[1][0])+abs(x[0][1]-x[1][1]));A,B=C,D=I[0],I[1];C,D=J[0],J[1];E,F=abs(C-A),abs(D-B);L=1 if A<C else-1;M=1 if B<D else-1;G=E-F
	while True:
		if g[A][B]==0:g[A][B]=3
		if A==C and B==D:break
		K=G*2
		if K>-F:G-=F;A+=L
		if K<E:G+=E;B+=M
	return g