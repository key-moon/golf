def PG(A,B):return type(B)(A(B)for B in B)
def PE(A):return type(A)(B for A in A for B in A)
def V(A):return min(A for(B,A)in J(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PY(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def G(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Y(A):return min(A for(A,B)in J(A))
def W(A,B,C,D):
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
	return PL(A,(-Y(A),-V(A)))
def PL(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def M(A,B):return frozenset((A,B)for B in J(B))
def PJ(A,B):return PE(PG(A,B))
def PR(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def K(A,B):return lambda x:A(x)==B
def R(A,B):return lambda x:A(B(x))
def PV(A,B):return PX(PU(B,A))
def PU(A,B):return type(B)(B for B in B if B!=A)
def PH(A):return max(enumerate(A))[1]
def PX(A):return next(iter(A))
def Q(A,B):return type(A)(A for A in A if B(A))
def PS(i):return i,0
def PP(A,B):return min(A,key=B)
def PZ(A,B):return max(A,key=B)
def PK(A):return len(A)
def P(a,b):return type(a)(A for A in a if A not in b)
def H(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));C=W(I,False,True,True);D=PZ(C,PK);J=PU(D,C);A=U(D);L=R(PH,PH);N=PQ(PP,L);B=R(PX,N);O=PR(PV,G,B);S=B(A);T=K(PX,S);E=Q(A,T);V=P(A,E);F=R(PS,Y);X=PM(PL,E);Z=PM(PL,V);a=R(X,F);b=R(Z,F);c=PR(M,B,a);d=PR(M,O,b);e=PR(H,c,d);f=PJ(e,J);g=PW(I,f);return[*map(list,g)]