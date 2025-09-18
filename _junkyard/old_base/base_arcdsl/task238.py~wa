def PW(A,B):return type(B)(B for B in B if B!=A)
def ZP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PY(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Q(A):return max(A for(A,B)in J(A))
def V(A):return min(A for(A,B)in J(A))
def M(A):return max(A for(B,A)in J(A))
def K(A):return min(A for(B,A)in J(A))
def PQ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-K(A)+1
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def ZY(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PK(A):return PM(A),PQ(A)
def PU(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PJ(A,B):return ZY(B,G(A),PK(A))
def ZJ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def ZL(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PS(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=G(A)[1]+R(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def X(A):return len(PY(A))
def W(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def PZ(A,B,C,D):
	M=L(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=Y if C else Z
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
	return PH(A,(-V(A),-K(A)))
def PH(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def R(A):return tuple(map(max,zip(*J(A))))
def G(A):return tuple(map(min,zip(*J(A))))
def ZE(A,B):return type(B)(A(B)for B in B)
def ZX(A,a,b):return lambda x:A(a(x),b(x))
def ZS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PG(h,g,f):return lambda x:h(g(f(x)))
def PE(A,B):return lambda x:A(B(x))
def PX(a,b):return a,b
def ZZ(A,B):return PR(PW(B,A))
def PR(A):return next(iter(A))
def PP(A):return frozenset({A})
def PV(A,B):return min(A,key=B)
def P(a,b):return a&b
def PL(a,b):return type(a)((*a,*b))
def H(x):return x
def p(I):I=tuple(map(tuple,I));B=PZ(I,False,True,True);C=PV(B,X);D=ZZ(B,C);E=PJ(D,I);F=U(C);K=PH(F,(1,1));A=J(K);L=U(D);M=ZS(PV,L);N=ZS(ZU,W);O=ZU(PE,PP);Q=PG(O,N,PP);S=PG(PR,M,Q);T=ZX(PX,S,H);V=ZE(T,A);Y=ZJ(E,V);Z=ZX(PU,G,R);a=Z(A);b=ZX(PL,H,PS);c=b(a);d=P(A,c);e=ZL(Y,8,d);return[*map(list,e)]