def p(g):
	I,J=len(g),len(g[0]);S=[];O=set()
	for D in range(I):
		for E in range(J):
			if g[D][E]==0 and(D,E)not in O:
				F=[(D,E)];C=[];T=True
				while F:
					A,B=F.pop()
					if(A,B)in O or not(0<=A<I and 0<=B<J)or g[A][B]!=0:continue
					O.add((A,B));C.append((A,B))
					if A in(0,I-1)or B in(0,J-1):T=False
					for(K,L)in((1,0),(-1,0),(0,1),(0,-1)):F.append((A+K,B+L))
				if T:S.append(C)
	M=[];P=set()
	for D in range(I):
		for E in range(J):
			U=g[D][E]
			if U not in(0,5)and(D,E)not in P:
				F=[(D,E)];C=[];G=U
				while F:
					A,B=F.pop()
					if(A,B)in P or not(0<=A<I and 0<=B<J)or g[A][B]!=G:continue
					P.add((A,B));C.append((A,B))
					for(K,L)in((1,0),(-1,0),(0,1),(0,-1)):F.append((A+K,B+L))
				M.append((G,C))
	def V(comp):A=comp;B=min(A for(A,B)in A);C=min(A for(B,A)in A);return set((A-B,D-C)for(A,D)in A),(B,C)
	W=[];X=[]
	for Z in S:Q,H=V(Z);W.append(Q);X.append(H)
	a=[];R=[];b=[]
	for(G,C)in M:Q,H=V(C);R.append(Q);b.append(H);a.append(G)
	Y=[None]*len(M)
	for(N,c)in enumerate(R):
		for(d,e)in enumerate(W):
			if c==e:Y[N]=d;break
	for(h,C)in M:
		for(A,B)in C:g[A][B]=0
	for(N,(G,C))in enumerate(M):
		f=1-Y[N];H=X[f]
		for(K,L)in R[N]:g[H[0]+K][H[1]+L]=G
	return g