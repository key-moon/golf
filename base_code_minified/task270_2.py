def p(g):
	A={}
	for(J,K)in enumerate(g):
		for(L,C)in enumerate(K):C and A.setdefault(C,[]).append((J,L))
	M=sorted([A for(A,B)in A.items()if len(B)==1]);N=sorted([A for(A,B)in A.items()if len(B)==4],reverse=1);B=[[0]*len(g[0])for A in g]
	for(D,O)in zip(N,M):
		E=A[D];F=[A for(A,B)in E];G=[A for(B,A)in E];H=[A for A in set(F)if F.count(A)==2][0];I=[A for A in set(G)if G.count(A)==2][0];B[H][I]=O
		for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):B[H+P][I+Q]=D
	return B