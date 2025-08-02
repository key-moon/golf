def p(g):
	A={}
	for G in g:
		for M in G:A[M]=A.get(M,0)+1
	B=sorted(A);N=B[0];H=B[-1];O=N if A[N]>A[H]else H;P=B[1]if O==H else B[-2];Q=set(B)-{O,P};I,J=len(g),len(g[0]);C,K,D,L=I,-1,J,-1
	for E in range(I):
		for F in range(J):
			if g[E][F]in Q:C=min(C,E);K=max(K,E);D=min(D,F);L=max(L,F)
	R,G=K-C+1,L-D+1;S=[(A,B,g[C+A][D+B])for A in range(R)for B in range(G)if g[C+A][D+B]in Q]
	for T in range(I-R+1):
		for U in range(J-G+1):
			if all(g[T+A][U+B]==P for(A,B,C)in S):
				for(E,F,V)in S:g[T+E][U+F]=V
	return g