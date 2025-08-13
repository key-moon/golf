def G(A,B):return type(A)(A for A in A if B(A))
def K(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in U(a)for(C,D)in U(b))
def R(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def Y(a,b):return E(a,b)==1
def W(A,B,C,D):
	M=J(A)if D else None;N=set();G=set();Q,R=len(A),len(A[0]);S=X(A);T=L if C else Z
	for E in S:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==M:continue
		O={(H,E)};I={E}
		while len(I)>0:
			P=set()
			for F in I:
				K=A[F[0]][F[1]]
				if H==K if B else K!=M:O.add((K,F));G.add(F);P|={(A,B)for(A,B)in T(F)if 0<=A<Q and 0<=B<R}
			I=P-G
		N.add(frozenset(O))
	return frozenset(N)
def M(A,B):return frozenset((A,B)for B in U(B))
def Q(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def H(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def V(A,B):return K(G(A,B))
def p(I):A=False;I=tuple(map(tuple,I));B=W(I,True,A,A);C=P(B,0);D=Q(I,1);E=H(Y,D);F=V(C,E);G=M(1,F);J=R(I,G);return[*map(list,J)]