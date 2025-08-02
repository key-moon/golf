def p(A):
	B=len(A);F=[[0]*B for A in range(B)];C=[(C,D)for C in range(B)for D in range(B)if A[C][D]and A[C][D]!=5];G=A[C[0][0]][C[0][1]];D,E=next((B,C)for(B,C)in C if 5 in A[B]);I=1 if A[D].index(5)>E else-1;J=max(A.count(5)for A in A)+2
	for(D,E)in C:F[D][E]=G;H=E+I*J;0<=H<B and F[D].__setitem__(H,G)
	return F