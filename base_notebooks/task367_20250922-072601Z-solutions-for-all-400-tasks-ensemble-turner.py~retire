def p(I):
	E,F=len(I),len(I[0])
	def J(g,c):
		G=[[0]*F for A in range(E)];J=[]
		for A in range(E):
			for B in range(F):
				if G[A][B]or g[A][B]!=c:G[A][B]=1;continue
				G[A][B]=1;H=[(A,B)];I=0;K=[(A,B)]
				while I<len(H):C,D=H[I];I+=1;[H.append((C+A,D+B))or K.append((C+A,D+B))or G[C+A].__setitem__(D+B,1)for(A,B)in[(1,0),(-1,0),(0,1),(0,-1)]if 0<=C+A<E and 0<=D+B<F and not G[C+A][D+B]and g[C+A][D+B]==c]
				J.append(K)
		return J
	A=lambda L:(min(A for(A,B)in L),min(A for(B,A)in L),max(A for(A,B)in L),max(A for(B,A)in L));K=lambda L:(lambda u,l,d,r:len(L)==(d-u+1)*(r-l+1))(*A(L));L=lambda L:(lambda u,l,d,r:{(A,l-1)for A in range(u-1,d+2)}|{(A,r+1)for A in range(u-1,d+2)}|{(u-1,A)for A in range(l-1,r+2)}|{(d+1,A)for A in range(l-1,r+2)})(*A(L));M={(A,B)for A in range(E)for B in range(F)if I[A][B]==5};C=set()
	for B in J(I,0):
		if K(B):D=L(B);G=set();[G.add((A+C,B+D))for(A,B)in(lambda u,l,d,r:{(u,l),(u,r),(d,l),(d,r)})(*A(list(D)))for(C,D)in[(1,0),(-1,0),(0,1),(0,-1)]];M.isdisjoint(G-D)and C.update(B)
	H=[list(A)for A in I];[H[A].__setitem__(B,4)for(A,B)in C if 0<=A<E and 0<=B<F];return[list(A)for A in H]