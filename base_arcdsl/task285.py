def ZR(A,B):return type(B)(A(B)for B in B)
def ZE(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def M(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in U(a)for(C,D)in U(b))
def W(A):return max(A for(A,B)in U(A))
def V(A):return max(A for(B,A)in U(A))
def G(A):return min(A for(B,A)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def ZU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-G(A)+1
def PR(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-Y(A)+1
def ZJ(A):return Y(A)+PR(A)//2,G(A)+ZU(A)//2
def H(A):return tuple(map(max,zip(*U(A))))
def Q(A):return tuple(map(min,zip(*U(A))))
def K(A):
	if len(A)==0:return frozenset({})
	B=U(A);C,D=Q(B);E,F=H(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def ZW(B):
	if len(B)==0:return frozenset({})
	return K(B)-U(B)
def ZM(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def PP(a,b):
	A,B=ZJ(U(a));C,D=ZJ(U(b))
	if A==C:return 0,1 if B<D else-1
	elif B==D:return 1 if A<C else-1,0
	elif A<C:return 1,1 if B<D else-1
	elif A>C:return-1,1 if B<D else-1
def ZG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PL(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Q(A)[1]+H(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PV(A):
	if isinstance(A,tuple):return A[::-1]
	B=Q(A)[0]+H(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def PZ(a,b):return M(a,b)==1
def PX(A,B,C,D):
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
def ZV(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PE(A,B):return frozenset((A,B)for B in U(B))
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def ZL(A):return PR(A),ZU(A)
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PH(A,B):return ZE(ZR(A,B))
def ZH(A,a,b):return lambda x:A(a(x),b(x))
def ZQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZK(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def ZX(h,g,f):return lambda x:h(g(f(x)))
def PW(A,B):return lambda x:A(B(x))
def ZZ(A,B):return B.union(frozenset({A}))
def SP(A):return max(enumerate(A))[1]
def ZY(A):return next(iter(A))
def PM(A,B):return next(A for A in A if B(A))
def PY(A,B):return type(A)(A for A in A if B(A))
def ZP(j):return 0,j
def PK(i):return i,0
def PQ(x):
	if isinstance(x,int):return 0 if x==0 else x+1 if x>0 else x-1
	return 0 if x[0]==0 else x[0]+1 if x[0]>0 else x[0]-1,0 if x[1]==0 else x[1]+1 if x[1]>0 else x[1]-1
def PU(A):return frozenset({A})
def Z(a,b):return type(a)(A for A in a if A not in b)
def P(a,b):return a&b
def PG(a,b):return type(a)((*a,*b))
def PJ(a,b):return a==b
def ZS(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def PS(x):return x
def p(I):I=tuple(map(tuple,I));D=PX(I,False,True,True);S=ZQ(ZK,PJ);T=ZK(PW,ZY);V=ZX(T,S,X);A=ZH(PY,PS,V);E=ZH(Z,PS,A);W=ZQ(ZK,PZ);Y=ZK(PW,PU);a=ZX(Y,W,E);b=ZH(PM,A,a);K=ZH(ZZ,b,E);c=ZQ(PE,0);d=ZX(c,ZW,K);e=ZH(PG,K,d);B=ZH(PP,A,E);L=ZX(PK,ZY,B);M=ZX(ZP,SP,B);f=ZH(R,ZL,L);g=ZH(R,ZL,M);h=ZH(R,ZL,B);i=ZH(ZV,PV,f);j=ZH(ZV,PL,g);k=PW(PV,PL);l=ZH(ZV,k,h);F=ZQ(PW,A);m=F(i);n=F(j);o=F(l);p=PW(PQ,ZS);G=ZQ(PW,p);q=G(L);r=G(M);s=G(B);N=ZH(ZV,m,q);O=ZH(ZV,n,r);Q=ZH(ZV,o,s);H=ZQ(ZM,I);C=ZQ(PW,U);J=C(e);t=C(N);u=C(O);v=C(Q);w=ZH(P,J,t);x=ZH(P,J,u);y=ZH(P,J,v);z=ZX(H,ZY,w);A0=ZX(H,ZY,x);A1=ZX(H,ZY,y);A2=ZH(PE,z,N);A3=ZH(PE,A0,O);A4=ZH(PE,A1,Q);A5=PH(A2,D);A6=PH(A3,D);A7=PH(A4,D);A8=ZG(I,A5);A9=ZG(A8,A6);AA=ZG(A9,A7);return[*map(list,AA)]