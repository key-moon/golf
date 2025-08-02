def p(A):
	G={}
	for(H,I)in enumerate(A):
		for(J,E)in enumerate(I):
			if E:G.setdefault(E,[]).append((H,J))
	for(K,F)in G.items():
		B={A for(A,B)in F};C={A for(B,A)in F}
		if len(B)>1 and len(C)>1:L,M,N,O=min(B),max(B)+1,min(C),max(C)+1;break
	D=[]
	for(E,F)in G.items():
		if E==K:continue
		B={A for(A,B)in F};C={A for(B,A)in F}
		if(len(B)==1)^(len(C)==1):D.append((E,B,C))
	P=M-L;Q=O-N;T,R,U=D[0]
	if len(R)==1:D.sort(key=lambda V:next(iter(V[1])));return[[A]*Q for(A,B,B)in D]
	D.sort(key=lambda V:next(iter(V[2])));S=[A for(A,B,B)in D];return[S]*P