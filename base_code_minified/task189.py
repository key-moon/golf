def p(g):
	D,E=len(g),len(g[0])
	for A in range(D):
		F=g[A][0]
		if F and g[A].count(F)==E:L=F;break
	for B in range(E):
		if all(g[A][B]==L for A in range(D)):break
	for G in(0,A+1):
		M=A if G<A else D-A-1
		for C in(0,B+1):
			N=B if C<B else E-B-1
			if M==2==N:O=[g[G][C:C+2],g[G+1][C:C+2]]
	H=[[0]*6 for A in[0]*6]
	for I in(0,1):
		for J in(0,1):
			P=O[I][J]
			for K in(1,3,4,5,7):H[3*I+K//3][3*J+K%3]=P
	return H