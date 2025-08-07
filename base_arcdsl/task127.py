def PX(A,B):return type(B)(A(B)for B in B)
def PS(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def V(A):return max(A for(A,B)in J(A))
def Y(A):return max(A for(B,A)in J(A))
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return min(A for(B,A)in J(A))
def L(A):return min(A for(A,B)in J(A))
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-M(A)+1
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PP(A):return L(A)+R(A)//2,M(A)+PZ(A)//2
def K(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PE(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PJ(A):return next(iter(A))[0]
def Q(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();Q,R=len(A),len(A[0]);S=U(A);T=X if C else P
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def X(A):return P(A)|Z(A)
def W(A,B):return frozenset((A,B)for B in J(B))
def S(A,n):return frozenset(A for A in A if len(A)==n)
def H(A,B):return PS(PX(A,B))
def PL(A,a,b):return lambda x:A(a(x),b(x))
def G(A,B):return lambda x:A(B(x))
def p(I):I=tuple(map(tuple,I));A=Q(I,True,False,True);B=S(A,1);C=G(X,PP);D=PL(W,PJ,C);E=H(D,B);F=PE(I,E);J=K(F,1,6);L=K(J,2,7);M=K(L,3,8);N=K(M,4,9);return[*map(list,N)]