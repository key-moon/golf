def ZJ(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def ZM(A):return type(A)(B for A in A for B in A)
def K(A):return max(A for(B,A)in X(A))
def PP(A):return min(A for(B,A)in X(A))
def Q(A):return min(A for(A,B)in X(A))
def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def M(A):return J(A)|U(A)
def J(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def Y(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PW(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PS(A):return tuple(map(max,zip(*X(A))))
def ZH(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def X(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def H(A):return tuple(map(min,zip(*X(A))))
def ZE(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def SZ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PQ(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return PV(PH(PV(A)))
def PH(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=H(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PV(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=H(A)[1]+PS(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PM(A):
	if isinstance(A,tuple):return A[::-1]
	B=H(A)[0]+PS(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def ZG(A):return tuple(A for A in zip(*A[::-1]))
def ZW(A):return next(iter(A))[0]
def P(A):return tuple(map(lambda x:sum(x)//len(A),zip(*X(A))))
def R(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in X(a)for(C,D)in X(b))
def S(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PW(A)-{V(A)})
def PL(A,B,C,D):
	L=V(A)if D else None;N=set();G=set();Q,R=len(A),len(A[0]);S=Y(A);T=M if C else J
	for E in S:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==L:continue
		O={(H,E)};I={E}
		while len(I)>0:
			P=set()
			for F in I:
				K=A[F[0]][F[1]]
				if H==K if B else K!=L:O.add((K,F));G.add(F);P|={(A,B)for(A,B)in T(F)if 0<=A<Q and 0<=B<R}
			I=P-G
		N.add(frozenset(O))
	return frozenset(N)
def L(A):
	if len(A)==0:return A
	return ZK(A,(-Q(A),-PP(A)))
def ZK(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Z(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def ZV(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return K(A)-PP(A)+1
def V(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PE(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def PY(A,a,b):return ZM(ZJ(A,a,b))
def SJ(A,B):return type(B)(A(B)for B in B)
def SE(A,a,b):return lambda x:A(a(x),b(x))
def SP(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def SS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def ZQ(h,g,f):return lambda x:h(g(f(x)))
def PG(A,B):return lambda x:A(B(x))
def ZZ(A,a,b):return a if A else b
def SX(a,b):return tuple(zip(a,b))
def PK(a,b):return a,b
def PZ(A,B,C):return tuple(range(A,B,C))
def ZY(A,B):return type(B)(B for B in B if B!=A)
def ZX(A,B):return B.union(frozenset({A}))
def PJ(x):return x>0
def G(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def E(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PX(A):return frozenset({A})
def ZS(A,B):return min(A,key=B)
def ZP(A,B):return B(max(A,key=B,default=0))
def PR(Aa):return min(Aa,default=0)
def SU(A):return len(A)
def ZR(A,B):return tuple(sorted(A,key=B))
def W(A,B):return A in B
def ZU(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def ZL(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def SL(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def PU(x):return x
def p(I):I=tuple(map(tuple,I));J=V(I);B=S(I);K=PL(I,True,False,True);M=SS(ZP,ZV);N=SP(Z,K);O=PG(N,ZW);Q=PG(ZU,M);T=SP(PE,R);U=SE(T,PU,PU);X=SP(ZY,0);Y=PG(X,U);a=SS(ZZ,-2);b=SE(a,PJ,G);c=ZQ(b,PR,Y);d=SE(SL,c,Q);e=PG(d,O);f=PG(ZL,e);g=ZR(B,f);h=SS(ZS,P);i=PG(PX,PV);j=SE(ZX,PH,i);k=SE(ZX,PQ,j);l=SE(ZX,PM,k);m=PG(h,l);n=SJ(m,g);C=SU(B);o=SJ(SU,B);p=W(1,o);q=E(C);D=ZZ(p,C,q);r=ZU(D);F=G(r);s=SJ(L,n);H=PZ(0,D,1);t=SX(H,H);A=PY(ZK,s,t);u=PK(F,F);v=ZE(J,u);w=SZ(v,A);x=ZG(w);y=SZ(x,A);z=ZG(y);A0=SZ(z,A);A1=ZG(A0);A2=SZ(A1,A);return[*map(list,A2)]