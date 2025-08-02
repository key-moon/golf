def p(A):
	E=[(B,C)for B in range(10)for C in range(10)if A[B][C]];I=[A for A in E if not any(abs(A[0]-B[0])+abs(A[1]-B[1])==1 for B in E)];J,B=I;C,D=J;K=A[C][D];L=(B[0]>C)-(B[0]<C);M=(B[1]>D)-(B[1]<D)
	for F in range(-10,10):
		G,H=C+L*F,D+M*F
		if 0<=G<10 and 0<=H<10:A[G][H]=K
	return A