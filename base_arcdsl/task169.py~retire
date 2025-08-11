def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A,B,C,D):
	M=J(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=X if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			P=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			K=P-H
		N.add(frozenset(O))
	return frozenset(N)
def P(A,n):return frozenset(A for A in A if len(A)==n)
def M(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def L(A,B):return lambda x:A(B(x))
def V(A):return type(A)(B for A in A for B in A)
def p(I):I=tuple(map(tuple,I));B=Y(I,True,False,True);C=M(P,B);A=L(V,C);D=A(2);E=A(3);F=A(4);G=Q(I,3,D);H=Q(G,2,E);J=Q(H,1,F);return[*map(list,J)]