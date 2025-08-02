def p(g):
	D={}
	for(P,Q)in enumerate(g):
		for(R,E)in enumerate(Q):
			if E:D.setdefault(E,[]).append((P,R))
	S=sorted(D.items(),key=lambda t:min(A for(B,A)in t[1]));F=[]
	for(T,G)in S:H,I=zip(*G);J,K=min(H),min(I);U,V=max(H)-J+1,max(I)-K+1;F.append((T,[(A-J,B-K)for(A,B)in G],U,V))
	(W,L,X,X),(Y,M,Z,a)=F;b=set(L)
	for(N,O)in((0,3-a),(3-Z,0)):
		if all((A+N,B+O)not in b for(A,B)in M):break
	A=[[0]*3 for A in range(3)]
	for(B,C)in L:A[B][C]=W
	for(B,C)in M:A[B+N][C+O]=Y
	return A