def ZL(A,B):return type(B)(A(B)for B in B)
def PH(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Q(A):return max(A for(A,B)in U(A))
def W(A):return max(A for(B,A)in U(A))
def PR(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-G(A)+1
def PQ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def ZU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A):return min(A for(B,A)in U(A))
def V(A):return min(A for(A,B)in U(A))
def E(A):
	if len(A)==0:return A
	return ZJ(A,(-V(A),-G(A)))
def ZZ(A):return PQ(A),PR(A)
def P(A,B):
	C=set();L=E(B);D,F=len(A),len(A[0]);M,N=ZZ(B);O,P=D-M+1,F-N+1
	for G in range(O):
		for H in range(P):
			I=True
			for(Q,(J,K))in ZJ(L,(G,H)):
				if not(0<=J<D and 0<=K<F and A[J][K]==Q):I=False;break
			if I:C.add((G,H))
	return frozenset(C)
def PK(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def ZM(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PP(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PS(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in U(A)if 0<=A<D and 0<=C<E)
def PX(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def M(A,B):return V(A)==0 or G(A)==0 or Q(A)==len(B)-1 or W(A)==len(B[0])-1
def L(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def ZJ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PL(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Z(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def PG(A,B):return PH(ZL(A,B))
def ZV(A,a,b):return lambda x:A(a(x),b(x))
def ZE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PY(A,B):return lambda x:A(x)==B
def ZP(h,g,f):return lambda x:h(g(f(x)))
def PV(A,B):return lambda x:A(B(x))
def PE(a,b):return frozenset((B,A)for A in b for B in a)
def PM(a,b):return a,b
def R(A,B,C):return tuple(range(A,B,C))
def ZW(A):return max(enumerate(A))[1]
def ZS(A):return next(iter(A))
def PU(A,B):return type(A)(A for A in A if B(A))
def H(x):return x>0
def ZQ(a,b):return a and b
def PJ(A):return frozenset({A})
def PW(A,B):return max(A,key=B)
def ZY(A):return len(A)
def Y(A,B):return A in B
def K(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def PZ(x):return x
def p(I):I=tuple(map(tuple,I));J=X(I);N=ZV(PE,PZ,PZ);O=ZE(PK,0);B=PV(PP,O);Q=ZV(K,ZS,ZW);T=PV(H,ZY);U=ZE(ZE,ZJ);V=ZX(ZV,Q);W=ZE(V,K);a=ZE(ZP,T);b=ZX(a,B);c=ZE(ZE,P);d=ZP(W,b,c);e=PV(N,ZS);f=PV(d,ZW);D=ZV(PW,e,f);g=ZP(U,B,D);h=PV(B,D);i=ZV(P,ZW,h);C=ZV(PG,g,i);j=K(2,6);k=R(3,j,1);l=PM(k,I);m=C(l);E=ZM(I,3,m);F=R(3,10,1);n=PM(F,E);o=C(n);G=ZM(E,3,o);p=PM(F,G);q=C(p);r=ZM(G,3,q);s=ZX(PS,r);t=ZX(Z,3);u=ZP(t,s,L);v=PY(u,8);w=PU(J,v);A=ZM(I,3,w);x=PL(A,0);y=ZX(M,A);z=PV(y,PJ);A0=ZE(Y,3);A1=ZX(PS,A);A2=ZP(A0,PX,A1);A3=PV(A2,S);A4=ZV(ZQ,A3,z);A5=PU(x,A4);A6=ZM(A,3,A5);return[*map(list,A6)]