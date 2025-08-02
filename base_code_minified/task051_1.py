def p(A):
	F,G=len(A),len(A[0]);I=sum(A,[]);J=list({*I}-{0});H=[A for A in J if I.count(A)==1][0];K=[A for A in J if A!=H][0]
	for B in range(F):
		for C in range(G):
			if A[B][C]==H:break
			else:break
	for(D,E)in[(-1,0),(1,0),(0,-1),(0,1)]:
		if 0<=B+D<F and 0<=C+E<G and A[B+D][C+E]==K:D,E=-D,-E;break
	while 0<=B+D<F and 0<=C+E<G:B+=D;C+=E;A[B][C]=H
	return A