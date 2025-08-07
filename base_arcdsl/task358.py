def Q(A):return max(A for(A,B)in U(A))
def M(A):return min(A for(A,B)in U(A))
def W(A):return max(A for(B,A)in U(A))
def G(A):return min(A for(B,A)in U(A))
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-G(A)+1
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-M(A)+1
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def ZP(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PY(A,B):return ZP(A,L(A),U(B))
def PG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def X(a,b):return len(set(A for(B,A)in U(a))&set(A for(B,A)in U(b)))>0
def V(a,b):return len(set(A for(A,B)in U(a))&set(A for(A,B)in U(b)))>0
def H(A,B,C,D):
	M=L(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);T=E(A);U=Y if C else S
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in U(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def Y(A):return S(A)|J(A)
def PM(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PZ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PV(A):return PJ(A),PX(A)
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PE(A,B):return PL(PK(A,B))
def PK(A,B):return type(B)(A(B)for B in B)
def PH(A,a,b):return lambda x:A(a(x),b(x))
def PR(A,n):
	if n==1:return A
	return PS(A,PR(A,n-1))
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PS(A,B):return lambda x:A(B(x))
def PP(A,B):return type(A)(A for A in A if B(A))
def PU(a,b):return a or b
def R(A):return frozenset({A})
def PL(A):return type(A)(B for A in A for B in A)
def P(a,b):return type(a)(A for A in a if A not in b)
def K(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));A=E(I);D=Z(I);F=H(I,True,False,True);B=PZ(I,D);C=PL(F);G=PV(C);J=Y((0,0));L=PQ(PE,Y);M=PR(L,2);N=M(J);O=PQ(K,G);Q=PQ(PM,C);S=PK(O,N);T=PE(Q,S);U=PQ(V,B);W=PQ(X,B);a=PH(PU,U,W);b=PS(a,R);c=PG(I,T);d=PP(A,b);e=P(A,d);f=PY(c,e);return[*map(list,f)]