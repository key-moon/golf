def p(A):
	E,F=len(A),len(A[0])
	for B in range(E):
		G=A[B][0]
		if G and A[B].count(G)==F:M=G;break
	for C in range(F):
		if all(A[B][C]==M for B in range(E)):break
	for H in(0,B+1):
		N=B if H<B else E-B-1
		for D in(0,C+1):
			O=C if D<C else F-C-1
			if N==2==O:P=[A[H][D:D+2],A[H+1][D:D+2]]
	I=[[0]*6 for A in[0]*6]
	for J in(0,1):
		for K in(0,1):
			Q=P[J][K]
			for L in(1,3,4,5,7):I[3*J+L//3][3*K+L%3]=Q
	return I