def p(A):
	B,G=len(A),len(A[0]);E=[(B,C)for B in range(B)for C in range(G)if A[B][C]==5]
	for C in range(1,B):
		if any(0<=D-C<B and A[D-C][E]==2 for(D,E)in E):break
	for(H,F)in E:
		D=H-C
		if 0<=D<B and A[D][F]==2:A[D][F]=1
	return A