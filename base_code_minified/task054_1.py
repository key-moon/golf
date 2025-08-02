def p(g):
	E,P=len(g),len;F=P(g[0])
	for A in range(E):
		for B in range(F):
			C=g[A][B]
			if A and A<E-1 and B and B<F-1 and g[A-1][B]==C==g[A+1][B]and g[A][B-1]==C==g[A][B+1]:G,H,K=C and(A,B,C);break
		else:continue
		break
	for D in range(1,F):
		if g[G][H+D]!=K:break
	L=D-1;M=g[G][H+D]
	for D in range(1,E):
		if g[G+D][H]!=K:break
	N=D-1;O=[]
	for I in range(-N,N+1):
		for J in range(-L,L+1):
			if g[G+I][H+J]!=M:O.append((I,J,g[G+I][H+J]))
	for A in range(E):
		for B in range(F):
			if g[A][B]!=M and all(not(0<=C<E and 0<=D<F and g[C][D]==g[A][B])for(C,D)in((A-1,B),(A+1,B),(A,B-1),(A,B+1))):Q,R=A,B;break
		else:continue
		break
	for(S,T,C)in O:g[Q+S][R+T]=C
	return g