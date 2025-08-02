def p(g):
	A,B=len(g),len(g[0]);I=[(A,C,g[A][C])for A in range(A)for C in range(B)if g[A][C]];E,C,L=I[0];F,G,M=I[1];D,J=abs(G-C),abs(F-E);K=D==0 or D>J
	if K:g=list(map(list,zip(*g)));E,C,F,G=C,E,G,F;A,B=B,A;D=J
	H=[[0]*B for A in range(A)];N=[L,M]
	for(O,P)in enumerate(range(C,B,D)):
		for Q in range(A):H[Q][P]=N[O&1]
	return list(map(list,zip(*H)))if K else H