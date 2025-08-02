def p(g):
	E,F=len(g),len(g[0]);I=[(A,B)for A in range(E)for B in range(F)if g[A][B]==2];J=[(A,B)for A in range(E)for B in range(F)if g[A][B]==3];A=min(J,key=lambda a:min(abs(a[0]-A[0])+abs(a[1]-A[1])for A in I));D=min(I,key=lambda b:abs(b[0]-A[0])+abs(b[1]-A[1]));G=(D[0]>A[0])-(D[0]<A[0]);H=(D[1]>A[1])-(D[1]<A[1]);B,C=A
	while 0<=B+G<E and g[B+G][C]!=8:B+=G;g[B][C]=3
	while 0<=C+H<F and g[B][C+H]!=8:C+=H;g[B][C]=3
	return g