def p(A):
	B=len(A);D=[(B,C)for B in range(B)for C in range(len(A[0]))if A[B][C]==3];E=min(A for(A,B)in D)+.5;F=min(A for(B,A)in D)+.5
	for G in range(B):
		for H in range(len(A[0])):
			C=A[G][H]
			if C and C!=3:
				K=G-E;L=H-F
				for(M,N)in((1,1),(1,-1),(-1,1),(-1,-1)):
					I=int(E+M*K);J=int(F+N*L)
					if 0<=I<B and 0<=J<len(A[0]):A[I][J]=C
	return A