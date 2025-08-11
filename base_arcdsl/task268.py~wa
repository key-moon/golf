def ZJ(A):return type(A)(B for A in A for B in A)
def ZL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return S(A)|J(A)
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in U(a)for(C,D)in U(b))
def W(A):return max(A for(A,B)in U(A))
def V(A):return max(A for(B,A)in U(A))
def G(A):return min(A for(B,A)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def ZS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-G(A)+1
def PH(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-Y(A)+1
def ZZ(A):return Y(A)+PH(A)//2,G(A)+ZS(A)//2
def PE(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*U(A)))))
def PZ(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*U(A)))))
def K(A):
	if len(A)==0:return frozenset({})
	B=U(A);C,D=Q(B);E,F=PP(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def PP(A):return tuple(map(max,zip(*U(A))))
def Q(A):return tuple(map(min,zip(*U(A))))
def PQ(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def ZM(A,B):return PQ(A,(A[0]+42*B[0],A[1]+42*B[1]))
def SP(A):
	if len(A)==0:return A
	F,G=Q(A);H,I=PP(A);B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def ZY(B):
	if len(B)==0:return frozenset({})
	return K(B)-U(B)
def PL(A):return frozenset({Q(A),PZ(A),PE(A),PP(A)})
def PJ(a,b):
	A,B=ZZ(U(a));C,D=ZZ(U(b))
	if A==C:return 0,1 if B<D else-1
	elif B==D:return 1 if A<C else-1,0
	elif A<C:return 1,1 if B<D else-1
	elif A>C:return-1,1 if B<D else-1
def ZK(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PX(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in U(A)if 0<=A<D and 0<=C<E)
def PU(a,b):return M(a,b)==1
def PV(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);T=E(A);U=L if C else S
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
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def ZX(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PG(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Z(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def ZP(A,B):return ZJ(ZQ(A,B))
def ZQ(A,B):return type(B)(A(B)for B in B)
def ZG(A,a,b):return lambda x:A(a(x),b(x))
def ZV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZW(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PK(A,B):return lambda x:A(x)==B
def ZU(h,g,f):return lambda x:h(g(f(x)))
def PR(A,B):return lambda x:A(B(x))
def PW(a,b):return frozenset((B,A)for A in b for B in a)
def H(A,B,C):return tuple(range(A,B,C))
def ZR(A):return max(enumerate(A))[1]
def ZE(A):return next(iter(A))
def PM(A,B):return type(A)(A for A in A if B(A))
def ZH(a,b):return a and b
def PY(A):return frozenset({A})
def P(a,b):return type(a)(A for A in a if A not in b)
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def PS(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));F=PV(I,True,False,True);A=ZP(U,F);G=SP(A);B=P(G,A);D=ZY(A);J=PJ(D,B);K=H(0,9,1);L=ZV(R,J);M=ZQ(L,K);N=ZV(ZX,B);E=ZP(N,M);O=ZK(I,4,D);C=ZK(O,4,E);Q=PL(B);T=PG(C,0);V=ZW(PX,C);W=ZW(Z,0);X=ZU(W,V,S);Y=PK(X,2);a=ZW(PU,A);b=ZW(PU,E);c=ZG(ZH,a,b);d=PR(c,PY);e=PM(T,Y);f=PM(e,d);g=PW(Q,f);h=ZG(PS,ZR,ZE);i=ZG(ZM,ZE,h);j=ZP(i,g);k=ZK(C,4,j);return[*map(list,k)]