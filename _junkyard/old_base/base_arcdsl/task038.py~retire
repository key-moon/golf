def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def M(a,b):return tuple(A+B for(A,B)in zip(a,b))
def V(A,B,C,D):
	L=U(A)if D else None;M=set();H=set();P,Q=len(A),len(A[0]);R=E(A);T=X if C else S
	for F in R:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in T(G)if 0<=A<P and 0<=B<Q}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def Z(A,n):return frozenset(A for A in A if len(A)==n)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def Y(a,b):return a,b
def Q(A):return len(A)
def L(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));B=V(I,True,False,True);C=P(B,1);D=Z(C,4);A=Q(D);E=L(5,A);F=Y(1,A);G=W(1,F);H=Y(1,E);J=W(0,H);K=M(G,J);return[*map(list,K)]