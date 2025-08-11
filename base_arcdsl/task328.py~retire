def PQ(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def V(A):return max(A for(A,B)in J(A))
def Y(A):return max(A for(B,A)in J(A))
def PH(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return min(A for(B,A)in J(A))
def L(A):return min(A for(A,B)in J(A))
def PW(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-M(A)+1
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PV(A):return L(A)+PL(A)//2,M(A)+PW(A)//2
def ZZ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PG(A):return next(iter(A))[0]
def H(A,B,C,D):
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
def R(A,B):return frozenset((A,B)for B in J(B))
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PY(A,B):return PQ(ZJ(A,B))
def ZJ(A,B):return type(B)(A(B)for B in B)
def ZU(A,a,b):return lambda x:A(a(x),b(x))
def ZP(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PK(h,g,f):return lambda x:h(g(f(x)))
def PS(A,B):return lambda x:A(B(x))
def PJ(a,b):return a,b
def PM(A,B):return type(B)(B for B in B if B!=A)
def ZL(A):return max(enumerate(A))[1]
def PR(A):return next(iter(A))
def PP(A,B):return type(A)(A for A in A if B(A))
def ZX(x):
	if isinstance(x,int):return 0 if x==0 else 1 if x>0 else-1
	return 0 if x[0]==0 else 1 if x[0]>0 else-1,0 if x[1]==0 else 1 if x[1]>0 else-1
def PE(A,B):return min(A,key=B)
def PX(A,B):return B(min(A,key=B,default=0))
def PU(A):return max(A,default=0)
def PZ(a,b):return a>b
def P(a,b):return a&b
def K(a,b):return a==b
def ZE(n):return n%2==0
def W(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def Q(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def ZY(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def G(x):return x
def p(I):I=tuple(map(tuple,I));L=U(I);A=H(I,True,False,True);M=ZU(W,ZX,G);C=ZP(ZJ,M);N=PK(ZE,PU,C);B=ZP(PP,L);O=ZU(ZY,PR,ZL);S=ZS(PM,A);T=PS(PV,ZL);D=ZU(Q,PR,T);V=PS(N,D);X=ZP(ZS,K);Y=ZP(PE,A);Z=PK(O,C,D);a=ZP(ZP,PJ);E=ZP(ZS,PJ);b=ZP(PS,V);F=ZP(PS,Z);J=PS(F,a);c=PS(F,E);d=PS(Y,J);e=ZS(PS,d);f=ZP(ZP,PX);g=ZS(PS,J);h=PK(g,f,S);i=ZP(ZU,PZ);j=ZU(i,h,c);k=PK(B,b,E);l=PK(B,e,X);m=ZU(P,k,l);n=PS(B,j);o=ZU(P,m,n);p=ZU(R,PG,o);q=PY(p,A);r=ZZ(I,q);return[*map(list,r)]