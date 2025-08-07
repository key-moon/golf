def PX(A,B):return type(B)(A(B)for B in B)
def PZ(A):return type(A)(B for A in A for B in A)
def M(A):return min(A for(B,A)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return tuple(map(max,zip(*J(A))))
def W(A):
	if len(A)==0:return frozenset({})
	B=J(A);C,D=V(B);E,F=Q(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def PE(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def G(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in J(A)if 0<=A<D and 0<=C<E)
def K(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=L if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def U(A):
	if len(A)==0:return A
	return PS(A,(-Y(A),-M(A)))
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def V(A):return tuple(map(min,zip(*J(A))))
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PP(A,B):return PZ(PX(A,B))
def PU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def R(A,B):return lambda x:A(B(x))
def H(A,B):return min(A,key=B)
def PL(A):return len(A)
def p(I):B=False;I=tuple(map(tuple,I));C=K(I,True,B,B);A=P(C,0);D=H(A,PL);E=W(D);F=G(E,I);J=U(F);L=PU(PS,J);M=R(L,V);N=PP(M,A);O=PE(I,N);return[*map(list,O)]