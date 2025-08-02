def p(g):
	Q=len(g);N=len(g[0]);H={}
	for T in g:
		for R in T:H[R]=H.get(R,0)+1
	S=max(H,key=H.get);I=[[0]*N for A in g];U=[(1,0),(-1,0),(0,1),(0,-1)];O=[]
	for J in range(Q):
		for K in range(N):
			if g[J][K]!=S and not I[J][K]:
				A=[(J,K)];I[J][K]=1
				for(V,W)in A:
					for(B,C)in U:
						D,E=V+B,W+C
						if 0<=D<Q and 0<=E<N and g[D][E]!=S and not I[D][E]:I[D][E]=1;A.append((D,E))
				L,M=zip(*A);F,G,a,b=min(L),max(L),min(M),max(M);B=max(L)-min(L)+1;C=max(M)-min(M)+1;O.append((F,G,B,C,A))
	for(F,G,B,C,A)in O:
		if len(A)!=B*C or len({g[A][B]for(A,B)in A})>1:P=B,C,[(A-F,B-G,g[A][B])for(A,B)in A];break
	for(F,G,B,C,A)in O:
		if(B,C)==(P[0],P[1])and len(A)==B*C:
			for(X,Y,Z)in P[2]:g[F+X][G+Y]=Z
	return g