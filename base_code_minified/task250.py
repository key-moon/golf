def p(A):
	E=[A for(A,B)in enumerate(A)for C in B if C==2];F=[B for A in A for(B,C)in enumerate(A)if C==2];G,H=min(E),max(E);I,J=min(F),max(F);D=[[0]*len(A[0])for B in A]
	for(B,L)in enumerate(A):
		for(C,K)in enumerate(L):
			if K==2:D[B][C]=2
			if K==5:M=G-1 if B<G else H+1 if B>H else B;N=I-1 if C<I else J+1 if C>J else C;D[M][N]=5
	return D