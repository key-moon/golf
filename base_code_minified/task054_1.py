def p(A):
	F,Q=len(A),len;G=Q(A[0])
	for B in range(F):
		for C in range(G):
			D=A[B][C]
			if B and B<F-1 and C and C<G-1 and A[B-1][C]==D==A[B+1][C]and A[B][C-1]==D==A[B][C+1]:H,I,L=D and(B,C,D);break
		else:continue
		break
	for E in range(1,G):
		if A[H][I+E]!=L:break
	M=E-1;N=A[H][I+E]
	for E in range(1,F):
		if A[H+E][I]!=L:break
	O=E-1;P=[]
	for J in range(-O,O+1):
		for K in range(-M,M+1):
			if A[H+J][I+K]!=N:P.append((J,K,A[H+J][I+K]))
	for B in range(F):
		for C in range(G):
			if A[B][C]!=N and all(not(0<=D<F and 0<=E<G and A[D][E]==A[B][C])for(D,E)in((B-1,C),(B+1,C),(B,C-1),(B,C+1))):R,S=B,C;break
		else:continue
		break
	for(T,U,D)in P:A[R+T][S+U]=D
	return A