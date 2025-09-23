ZERO=0
ONE=1
FOUR=4
def solve_7df24a62(I):
	A=I;K,L=len(A),len(A[0])
	def M(grid,val):return{(A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==val}
	def G(coords):A=coords;B=min(A for(A,B)in A);C=min(A for(B,A)in A);return B,C
	def a(coords):
		A=coords
		if not A:return 0,0,-1,-1
		B=min(A for(A,B)in A);C=max(A for(A,B)in A);D=min(A for(B,A)in A);E=max(A for(B,A)in A);return B,D,C,E
	def b(grid):return tuple(tuple(A)for A in zip(*grid[::-1]))
	def c(grid):return tuple(tuple(A[::-1])for A in grid[::-1])
	def d(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
	def N(coords):
		A=coords
		if not A:return set()
		B,C=G(A);return{(A-B,D-C)for(A,D)in A}
	def e(coords):
		A=coords
		if not A:return 0,0
		B,C,D,E=a(A);return D-B+1,E-C+1
	def f(grid,val,coords):
		A=[list(A)for A in grid]
		for(B,C)in coords:
			if 0<=B<K and 0<=C<L:A[B][C]=val
		return tuple(tuple(A)for A in A)
	B=M(A,ONE);g=M(A,FOUR)
	if not B:return A
	O=min(A for(A,B)in B);h=max(A for(A,B)in B);P=min(A for(B,A)in B);i=max(A for(B,A)in B);Q=O,P;C=tuple(tuple(A[B][P:i+1])for B in range(O,h+1));H=[C,b(C),c(C),d(C)]
	def j(grid):return tuple(tuple(A[::-1])for A in grid)
	H+=[j(A)for A in H];R=set()
	for S in H:
		D={(A,C)for(A,B)in enumerate(S)for(C,D)in enumerate(B)if D==FOUR};J={(A,C)for(A,B)in enumerate(S)for(C,D)in enumerate(B)if D==ONE};s={(A+Q[0],B+Q[1])for(A,B)in D};k=g;T=G(D)if D else(0,0);U=G(J)if J else(0,0);l=U[0]-T[0];m=U[1]-T[1];V=N(D);n=N(J);W,X=e(V);Y=K-W+1;Z=L-X+1
		if Y<0 or Z<0:continue
		for E in range(Y):
			for F in range(Z):
				o={(A+E,B+F)for(A,B)in V};p={(A,B)for(A,B)in k if E<=A<E+W and F<=B<F+X}
				if p==o:q={(A+E+l,B+F+m)for(A,B)in n};R.update(q)
	r=f(A,ONE,R);return r
def _to_list_grid(grid):
	A=grid
	if isinstance(A,tuple):return[list(A)for A in A]
	return A
def p(g):return _to_list_grid(solve_7df24a62(g))