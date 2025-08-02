def p(g):
	F={}
	for(G,H)in enumerate(g):
		for(I,D)in enumerate(H):
			if D:F.setdefault(D,[]).append((G,I))
	for(J,E)in F.items():
		A={A for(A,B)in E};B={A for(B,A)in E}
		if len(A)>1 and len(B)>1:K,L,M,N=min(A),max(A)+1,min(B),max(B)+1;break
	C=[]
	for(D,E)in F.items():
		if D==J:continue
		A={A for(A,B)in E};B={A for(B,A)in E}
		if(len(A)==1)^(len(B)==1):C.append((D,A,B))
	O=L-K;P=N-M;S,Q,T=C[0]
	if len(Q)==1:C.sort(key=lambda t:next(iter(t[1])));return[[A]*P for(A,B,B)in C]
	C.sort(key=lambda t:next(iter(t[2])));R=[A for(A,B,B)in C];return[R]*O