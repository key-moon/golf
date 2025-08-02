def p(A):
	B,C=len(A),len(A[0]);J=[(B,D,A[B][D])for B in range(B)for D in range(C)if A[B][D]];F,D,M=J[0];G,H,N=J[1];E,K=abs(H-D),abs(G-F);L=E==0 or E>K
	if L:A=list(map(list,zip(*A)));F,D,G,H=D,F,H,G;B,C=C,B;E=K
	I=[[0]*C for A in range(B)];O=[M,N]
	for(P,Q)in enumerate(range(D,C,E)):
		for R in range(B):I[R][Q]=O[P&1]
	return list(map(list,zip(*I)))if L else I