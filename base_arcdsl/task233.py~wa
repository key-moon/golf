_A=True
def ZY(A):return type(A)(B for A in A for B in A)
def ZG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def H(A):return tuple(map(max,zip(*U(A))))
def SU(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def G(A):return max(A for(A,B)in U(A))
def W(A):return min(A for(A,B)in U(A))
def Q(A):return max(A for(B,A)in U(A))
def R(A):return min(A for(B,A)in U(A))
def ZL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Q(A)-R(A)+1
def ZJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return G(A)-W(A)+1
def ZM(A):return ZJ(A),ZL(A)
def P(A,B):
	C=set();L=E(B);D,F=len(A),len(A[0]);M,N=ZM(B);O,P=D-M+1,F-N+1
	for G in range(O):
		for H in range(P):
			I=_A
			for(Q,(J,K))in ZQ(L,(G,H)):
				if not(0<=J<D and 0<=K<F and A[J][K]==Q):I=False;break
			if I:C.add((G,H))
	return frozenset(C)
def ZU(A,a,b):return tuple(tuple(A if A!=a and A!=b else{a:b,b:a}[A]for A in A)for A in A)
def PV(A,B):return SU(B,K(A),ZM(A))
def ZR(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PQ(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return PE(ZP(PE(A)))
def ZP(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=K(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PE(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=K(A)[1]+H(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PM(A):
	if isinstance(A,tuple):return A[::-1]
	B=K(A)[0]+H(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def L(A):return len(PW(A))
def PW(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PU(A,B,C,D):
	K=Y(A)if D else None;L=set();G=set();O,P=len(A),len(A[0]);Q=X(A);R=V if C else S
	for E in Q:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		M={(H,E)};I={E}
		while len(I)>0:
			N=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:M.add((J,F));G.add(F);N|={(A,B)for(A,B)in R(F)if 0<=A<O and 0<=B<P}
			I=N-G
		L.add(frozenset(M))
	return frozenset(L)
def E(A):
	if len(A)==0:return A
	return ZQ(A,(-W(A),-R(A)))
def ZQ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PJ(A,B):return frozenset((A,B)for B in U(B))
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(A):return tuple(map(min,zip(*U(A))))
def Z(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def ZE(A,B):return ZY(SP(A,B))
def ZZ(A,B):return type(A)(A(B)for A in A)
def SP(A,B):return type(B)(A(B)for B in B)
def SS(A,a,b):return lambda x:A(a(x),b(x))
def ZK(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZH(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PG(A,B):return lambda x:A(x)==B
def ZV(h,g,f):return lambda x:h(g(f(x)))
def PK(A,B):return lambda x:A(B(x))
def PL(a,b):return frozenset((B,A)for A in b for B in a)
def PR(a,b):return a,b
def ZX(A,B):return type(B)(B for B in B if B!=A)
def SE(A):return max(enumerate(A))[1]
def ZW(A):return next(iter(A))
def PX(A,B):return type(A)(A for A in A if B(A))
def PP(x):return x>0
def ZS(A,B):return max(A,key=B)
def SZ(A):return len(A)
def PY(a,b):return a>b
def PH(a,b):return type(a)((*a,*b))
def M(A,B):return A in B
def PS(a,b):return a==b
def SJ(b):return not b
def PZ(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));A=PU(I,False,_A,_A);W=ZS(A,SZ);B=PV(W,I);X=ZH(PY,1);Y=PK(X,L);C=PX(A,Y);a=ZK(ZH,PZ);D=ZU(B,2,0);b=ZK(P,D);c=ZK(ZK,ZQ);d=PK(a,K);F=PG(ZW,2);e=PK(SJ,F);f=ZH(PX,F);g=ZH(PX,e);h=ZK(PJ,0);i=PK(h,g);G=SS(PH,i,f);H=ZV(d,G,E);j=PU(D,_A,_A,_A);k=SP(U,j);J=ZV(b,G,E);l=ZH(Z,2);N=ZK(PX,k);m=ZV(SZ,ZW,N);n=PK(PP,SZ);O=ZK(ZK,M);o=ZV(n,N,O);p=PK(m,O);q=ZH(PX,o);r=PK(q,J);s=ZK(ZH,PS);t=ZH(PK,p);u=ZV(t,s,l);v=SS(PX,r,u);w=SS(SP,H,v);Q=PK(c,E);x=SS(ZE,Q,w);y=PR(PQ,ZP);z=PR(PM,PE);R=PH(y,z);A0=PL(R,R);A1=SS(PK,ZW,SE);A2=SP(A1,A0);S=ZK(ZZ,A2);A3=ZE(S,C);T=ZE(x,A3);A4=ZR(B,T);A5=PW(T);V=ZK(ZX,2);A6=V(A5);A7=ZV(ZW,V,PW);A8=ZH(M,A6);A9=ZV(SJ,A8,A7);AA=PX(C,A9);AB=SS(SP,H,J);AC=SS(ZE,Q,AB);AD=ZE(S,AA);AE=ZE(AC,AD);AF=ZR(A4,AE);return[*map(list,AF)]