def p(A):
	B=[(B,C)for B in range(10)for C in range(10)if A[B][C]];I,J=min(B)[0],max(B)[0];K,L=min(B,key=lambda I:I[1])[1],max(B,key=lambda I:I[1])[1];E=I+J;F=K+L
	for(G,H)in B:
		M=A[G][H];C=2*G-E;D=2*H-F
		for(N,O)in((D,-C),(-C,-D),(-D,C)):A[(E+N)//2][(F+O)//2]=M
	return A