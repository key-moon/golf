def W(A):return max(A for(A,B)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def M(A):return max(A for(B,A)in J(A))
def Q(A):return min(A for(B,A)in J(A))
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-Q(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-Y(A)+1
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PX(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def G(A,B,C,D):
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
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PS(A):return PP(A),PZ(A)
def PE(A,B):return type(B)(A(B)for B in B)
def PU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def R(A,B):return lambda x:A(B(x))
def H(a,b):return a,b
def K(A,B):return next(A for A in A if B(A))
def V(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def L(A,B):return A in B
def p(I):B=False;I=tuple(map(tuple,I));C=PS(I);D=G(I,True,B,B);E=P(D,0);F=PE(J,E);M=PU(PU,L);N=PU(K,F);A=R(N,M);O=V(C);Q=H(5,5);S=A((0,0));T=A(O);U=A(Q);W=PX(I,1,S);X=PX(W,3,T);Y=PX(X,2,U);return[*map(list,Y)]