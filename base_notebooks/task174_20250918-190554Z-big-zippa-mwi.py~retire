def p(g):
	D,E=len(g),len(g[0]);from collections import Counter as G,deque;H=G(B for A in g for B in A).most_common(1)[0][0];C=[[False]*E for A in range(D)]
	def I(si,sj):
		J=g[si][sj];F=deque([(si,sj)]);C[si][sj]=True;G=[(si,sj)]
		while F:
			K,L=F.popleft()
			for H in(-1,0,1):
				for I in(-1,0,1):
					if H==0 and I==0:continue
					A,B=K+H,L+I
					if 0<=A<D and 0<=B<E and not C[A][B]and g[A][B]==J:C[A][B]=True;F.append((A,B));G.append((A,B))
		return G
	def J(cells):A=cells;B=[A for(A,B)in A];C=[A for(B,A)in A];D,E=min(B),max(B);F,G=min(C),max(C);return[A[F:G+1]for A in g[D:E+1]]
	def K(grid):return all(A==A[::-1]for A in grid)
	for A in range(D):
		for B in range(E):
			if g[A][B]!=H and not C[A][B]:
				L=I(A,B);F=J(L)
				if K(F):return[list(A)for A in F]
	return[list(A)for A in g]