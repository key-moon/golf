def p(A):
	G,H=len(A),len(A[0]);N=[B for A in A for B in A];O=max(set(N),key=N.count);I=[[0]*H for A in range(G)];P=[]
	for C in range(G):
		for D in range(H):
			if A[C][D]!=O and not I[C][D]:
				J=[(C,D)];I[C][D]=1;E=[]
				while J:
					Q,R=J.pop();E.append((Q,R))
					for(V,W)in((1,0),(-1,0),(0,1),(0,-1)):
						F,B=Q+V,R+W
						if 0<=F<G and 0<=B<H and not I[F][B]and A[F][B]!=O:I[F][B]=1;J.append((F,B))
				P.append(E)
	for E in P:
		X={A[B][C]for(B,C)in E}
		if len(X)>1:break
	Y=[A for(A,B)in E];Z=[A for(B,A)in E];S,T=min(Y),min(Z);K=[(B-S,C-T,A[B][C])for(B,C)in E];U={}
	for(L,M,B)in K:U.setdefault(B,[]).append((L,M))
	for(B,a)in U.items():
		b=min(a);c,d=b
		for C in range(G):
			for D in range(H):
				if A[C][D]==B and(C-S,D-T,B)not in K:
					e,f=C-c,D-d
					for(L,M,g)in K:A[e+L][f+M]=g
	return A