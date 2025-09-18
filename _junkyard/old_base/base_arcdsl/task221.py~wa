def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PL(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def K(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def H(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(PL(A,(0,B*C+C*E),(D,B))for C in range(n))
def M(a,b):return tuple(A+B for(A,B)in zip(a,b))
def PU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def V(A,B,C,D):
	M=U(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=J(A);T=E if C else Z
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
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def G(A,B):return PP(PX(A,B))
def PX(A,B):return type(B)(A(B)for B in B)
def PJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def W(A,B):return lambda x:A(B(x))
def Q(a,b):return a,b
def L(A,B,C):return tuple(range(A,B,C))
def PZ(A):return next(iter(A))
def R(j):return 0,j
def PP(A):return type(A)(B for A in A for B in A)
def X(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def Y(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):B=True;I=tuple(map(tuple,I));A=P(I,0);D=Y(9,A);E=X(A,3);F=X(E,A);J=Y(F,3);N=Q(3,J);O=K(0,N);C=M(I,O);S=V(C,B,B,B);T=PZ(S);U=PJ(PS,T);Z=W(U,R);a=L(0,D,1);b=PE(X,3);c=PX(b,a);d=G(Z,c);e=PU(C,d);f=H(e,A);g=PP(f);return[*map(list,g)]