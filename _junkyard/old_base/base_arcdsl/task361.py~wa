def H(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(A):return tuple(map(max,zip(*J(A))))
def PS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return tuple(map(min,zip(*J(A))))
def PU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def G(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=L(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def M(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=L(A)[1]+Y(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def W(A):
	if isinstance(A,tuple):return A[::-1]
	B=L(A)[0]+Y(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def V(A,B,C,D):
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
def PZ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def R(A,B):return H(PE(A,B))
def PE(A,B):return type(B)(A(B)for B in B)
def PJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def Q(A,B):return lambda x:A(B(x))
def PP(A):return next(iter(A))
def K(A,B):return max(A,key=B)
def PX(A):return len(A)
def P(a,b):return a&b
def p(I):F=False;A=True;I=tuple(map(tuple,I));H=V(I,F,A,A);J=X((0,0));B=R(X,J);C=PP(H);D=PJ(P,C);L=Q(W,M);N=L(C);O=PJ(PZ,N);S=PE(O,B);T=K(S,D);E=PU(I,T);U=V(E,F,A,A);Y=PP(U);Z=Q(PX,D);a=Q(M,G);b=a(Y);c=PJ(PZ,b);d=PE(c,B);e=K(d,Z);f=PU(E,e);return[*map(list,f)]