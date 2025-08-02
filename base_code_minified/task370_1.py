def p(g):
	D,E=len(g),len(g[0]);C=[(A,B)for A in range(D)for B in range(E)if g[A][B]==0]
	for(A,B)in C:
		if(A-1,B)in C and(A+1,B)in C and(A,B-1)in C and(A,B+1)in C:G,H=A,B;break
	K=g[0][0]
	for A in range(D):
		for B in range(E):
			if g[A][B]!=K and g[A][B]!=0:L,M,N=A,B,g[A][B];break
		else:continue
		break
	O,P=L-G,M-H;F=1
	while 1:
		I,J=G+O*F,H+P*F
		if not(0<=I<D and 0<=J<E):break
		g[I][J]=N;F+=1
	return g