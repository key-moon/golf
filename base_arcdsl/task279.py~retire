def R(A,B):return type(A)(A for A in A if B(A))
def PZ(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def V(A):return max(A for(B,A)in J(A))
def Q(A):return min(A for(B,A)in J(A))
def W(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def PS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PU(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A,B):return L(A)==0 or Q(A)==0 or W(A)==len(B)-1 or V(A)==len(B[0])-1
def G(a,b):return M(a,b)==1
def K(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();P,Q=len(A),len(A[0]);R=U(A);S=X if C else Z
	for F in R:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in S(G)if 0<=A<P and 0<=B<Q}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PP(A,B):return lambda x:A(B(x))
def H(A,B):return PZ(R(A,B))
def PE(b):return not b
def p(I):B=False;I=tuple(map(tuple,I));A=K(I,True,B,B);C=P(A,9);D=P(A,1);E=PJ(Y,I);F=PP(PE,E);J=H(C,F);L=PJ(G,J);M=H(D,L);N=PU(I,8,M);return[*map(list,N)]