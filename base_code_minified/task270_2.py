def p(A):
	B={}
	for(K,L)in enumerate(A):
		for(M,D)in enumerate(L):D and B.setdefault(D,[]).append((K,M))
	N=sorted([A for(A,B)in B.items()if len(B)==1]);O=sorted([A for(A,B)in B.items()if len(B)==4],reverse=1);C=[[0]*len(A[0])for B in A]
	for(E,P)in zip(O,N):
		F=B[E];G=[A for(A,B)in F];H=[A for(B,A)in F];I=[A for A in set(G)if G.count(A)==2][0];J=[A for A in set(H)if H.count(A)==2][0];C[I][J]=P
		for(Q,R)in((1,0),(-1,0),(0,1),(0,-1)):C[I+Q][J+R]=E
	return C