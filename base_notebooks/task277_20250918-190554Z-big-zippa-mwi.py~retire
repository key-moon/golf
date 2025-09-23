def p(g):
	G,H=len(g),len(g[0]);I={};[[I.update({A:I.get(A,0)+1})for A in A]for A in g];Q=max(I,key=I.get);K=[[0]*H for A in range(G)];L=[]
	for A in range(G):
		for B in range(H):
			if not K[A][B]and g[A][B]!=Q:
				C=[];M=[(A,B)];R=g[A][B]
				while M:
					D,E=M.pop()
					if 0<=D<G and 0<=E<H and not K[D][E]and g[D][E]==R:K[D][E]=1;C.append((D,E));M.extend([(D+A,E+B)for(A,B)in[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]])
				C and L.append(C)
	N=[]
	for C in L:
		if C:S,T=min(A[0]for A in C),min(A[1]for A in C);N.append([(A-S,B-T)for(A,B)in C])
	F={};[F.setdefault(tuple(sorted(B)),[]).append(A)for(A,B)in enumerate(N)]
	if F:U=min(F,key=lambda k:len(F[k]));O=F[U];P=L[O[0]]if O else[]
	else:P=[]
	J=[[1 if A==8 else A for A in A]for A in g]
	for(A,B)in P:0<=A<G and 0<=B<H and J.__setitem__(A,J[A][:B]+[2]+J[A][B+1:])
	return J