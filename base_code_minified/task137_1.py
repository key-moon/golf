def p(g):
	from math import gcd;K,L=len(g),len(g[0]);A=[(B,D,A)for(B,C)in enumerate(g)for(D,A)in enumerate(C)if A];M=A[0][2];B=sorted({A for(A,B,B)in A});C=sorted({B for(A,B,A)in A});D=0
	for(E,F)in zip(B,B[1:]):D=gcd(D,F-E)
	G=0
	for(E,F)in zip(C,C[1:]):G=gcd(G,F-E)
	H=max(D,G);N,O=B[0],C[0]
	for I in range(K):
		for J in range(L):g[I][J]=M if(I-N)%H==0 or(J-O)%H==0 else 0
	return g