def p(g):
	G,H=len(g),len(g[0]);W=sum(g,[]);J={};[J.update({A:J.get(A,0)+1})for A in W];X=max(J,key=J.get);O=[[0]*H for A in range(G)];T=[]
	for K in range(G):
		for L in range(H):
			if not O[K][L]and g[K][L]!=X:
				P=[];Q=[(K,L)];A=g[K][L]
				while Q:
					D,E=Q.pop()
					if D<0 or D>=G or E<0 or E>=H or O[D][E]or g[D][E]!=A:continue
					O[D][E]=1;P.append((D,E));Q.extend([(D+A,E+B)for(A,B)in[(0,1),(0,-1),(1,0),(-1,0)]])
				P and T.append(frozenset((A,B)for B in P))
	U,V=[],[]
	for C in T:
		I=[A for(B,A)in C]
		if I:R,Y,S,Z=min(A[0]for A in I),max(A[0]for A in I),min(A[1]for A in I),max(A[1]for A in I);M,N=Y-R+1,Z-S+1;a=[[g[R+A][S+B]if 0<=R+A<G and 0<=S+B<H else 0 for B in range(N)]for A in range(M)];b=[[a[A][B]for B in range(1,N-1)]for A in range(1,M-1)]if M>2 and N>2 else[];c=set(sum(b,[]));3 in c and U.append(C);len(C)==M+N-1 and V.append(C)
	F=[[6 if A==3 else A for A in A]for A in g]
	for C in U:
		for(d,(B,A))in C:0<=B<G and 0<=A<H and F.__setitem__(B,F[B][:A]+[2]+F[B][A+1:])
	for C in V:
		for(d,(B,A))in C:0<=B<G and 0<=A<H and F.__setitem__(B,F[B][:A]+[1]+F[B][A+1:])
	return F