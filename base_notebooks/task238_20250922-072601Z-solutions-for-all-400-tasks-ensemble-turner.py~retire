def p(g):
	def S(grid):
		B=grid
		if not B or not B[0]:return 0
		A={}
		for D in B:
			for C in D:A[C]=A.get(C,0)+1
		return max(A,key=A.get)
	def N(grid,univalued,diagonal,without_bg):
		L=univalued;A=grid
		if not A or not A[0]:return[]
		M,N=len(A),len(A[0]);O=S(A)if without_bg else None;P=[(-1,0),(1,0),(0,-1),(0,1)]
		if diagonal:P+=[(-1,-1),(-1,1),(1,-1),(1,1)]
		D,Q=set(),[]
		for E in range(M):
			for F in range(N):
				if(E,F)in D:continue
				R=A[E][F]
				if R==O:continue
				G,H=set(),[(E,F)]
				while H:
					B,C=H.pop()
					if(B,C)in D:continue
					I=A[B][C]
					if L and I!=R or not L and I==O:continue
					D.add((B,C));G.add((I,(B,C)))
					for(T,U)in P:
						J,K=B+T,C+U
						if 0<=J<M and 0<=K<N and(J,K)not in D:H.append((J,K))
				if G:Q.append(G)
		return Q
	def D(obj):
		A=obj
		if not A:return set()
		B=next(iter(A))
		if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,B)for(C,(A,B))in A}
		return set(A)
	def E(patch):
		A=D(patch)
		if not A:return(0,0),(0,0)
		B=min(A for(A,B)in A);C=min(A for(B,A)in A);E=max(A for(A,B)in A);F=max(A for(B,A)in A);return(B,C),(E,F)
	def I(obj):
		A=obj
		if not A:return A
		(B,C),D=E(A);return{(A,(D-B,E-C))for(A,(D,E))in A}
	def O(patch,d):
		A=patch;C,D=d
		if not A:return A
		B=next(iter(A))
		if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,(B+C,E+D))for(A,(B,E))in A}
		return{(A+C,B+D)for(A,B)in A}
	def P(a,b):
		A,B=a;C,D=b;E,F=min(A,C),min(B,D);G,H=max(A,C),max(B,D)
		if A==C:return{(A,B)for B in range(F,H+1)}
		if B==D:return{(A,B)for A in range(E,G+1)}
		if C-A==D-B:return{(A,B)for(A,B)in zip(range(E,G+1),range(F,H+1))}
		if C-A==B-D:return{(A,B)for(A,B)in zip(range(E,G+1),range(H,F-1,-1))}
		return set()
	def Q(idx):
		A=D(idx)
		if not A:return set()
		(B,C),(B,F)=E(A);G=C+F;return{(A,G-B)for(A,B)in A}
	F=N(g,univalued=False,diagonal=True,without_bg=True)
	if not F:return g
	R={(8,(A,C))for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==8};T=lambda o:len(D(o));U=R or min(F,key=lambda o:len({A for(A,B)in o}));V=[A for A in F if{A for(A,B)in A}!={8}]or F;G=max(V,key=T,default=None)
	if not G:return g
	J={(A,B)for(A,B)in G if A!=8};(W,X),(Y,Z)=E(J or G);a=[A[X:Z+1]for A in g[W:Y+1]];H=D(O(I(U),(1,1)));K=list(I(J or G));A=[list(A)for A in a]
	for(B,C)in H:
		if 0<=B<len(A)and 0<=C<len(A[0]):A[B][C]=min(K,key=lambda t:abs(t[1][0]-B)+abs(t[1][1]-C))[0]if K else 0
	L=E(H)
	if L!=((0,0),(0,0))and H:
		(b,c),(d,e)=L;M=P((b,c),(d,e));f=H&(M|Q(M))
		for(B,C)in f:
			if 0<=B<len(A)and 0<=C<len(A[0]):A[B][C]=8
	return A