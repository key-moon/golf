def V(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def Y(A):return max(A for(B,A)in J(A))
def M(A):return min(A for(B,A)in J(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-M(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PZ(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PL(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PM(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def W(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in J(A)if 0<=A<D and 0<=C<E)
def Q(A,B,C,D):
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
def X(A):return Z(A)|S(A)
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def PU(A):return PP(A),PS(A)
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PJ(h,g,f):return lambda x:h(g(f(x)))
def R(A,B):return lambda x:A(B(x))
def G(A,B):return type(A)(A for A in A if B(A))
def H(A,B):return max(A,key=B)
def PV(A):return len(A)
def K(a,b):return a>b
def p(I):I=tuple(map(tuple,I));C=PU(I);D=U(I);F=Q(I,True,False,True);A=H(F,PV);J=E(A);L=PZ(0,C);B=PL(L,A);M=PY(W,B);N=PY(P,J);O=PJ(N,M,X);S=PX(K,3);T=R(S,O);V=G(D,T);Y=PM(B,0,V);return[*map(list,Y)]