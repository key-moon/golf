def s4(I):
	C,D=len(I),len(I[0])
	def L(grid,color):
		J=color;G=[[False]*D for A in range(C)];K=[]
		for E in range(C):
			for F in range(D):
				if G[E][F]:continue
				G[E][F]=True
				if grid[E][F]!=J:continue
				H=[(E,F)];I=0;L=[(E,F)]
				while I<len(H):
					M,N=H[I];I+=1
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=M+O,N+P
						if 0<=A<C and 0<=B<D and not G[A][B]:
							G[A][B]=True
							if grid[A][B]==J:H.append((A,B));L.append((A,B))
				K.append(L)
		return K
	def A(cells):A=cells;B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
	def M(cells):B=cells;C,D,E,F=A(B);G=(E-C+1)*(F-D+1);return len(B)==G
	def N(cells):F,G,H,I=A(cells);B,C=F-1,G-1;D,E=H+1,I+1;J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return J|K
	def O(rect):B,C,D,E=A(list(rect));return{(B,C),(B,E),(D,C),(D,E)}
	P={(A,B)for A in range(C)for B in range(D)if I[A][B]==5};F=set()
	for B in L(I,0):
		if not M(B):continue
		G=N(B);E=set()
		for(Q,R)in O(G):
			for(S,T)in((1,0),(-1,0),(0,1),(0,-1)):U,V=Q+S,R+T;E.add((U,V))
		E-=G
		if P.isdisjoint(E):F.update(B)
	H=[list(A)for A in I]
	for(J,K)in F:
		if 0<=J<C and 0<=K<D:H[J][K]=4
	return tuple(tuple(A)for A in H)
def p(g):A=tuple(tuple(A)for A in g);B=s4(A);return[list(A)for A in B]