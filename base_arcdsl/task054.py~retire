_A=False
def ZX(A,B):return type(B)(A(B)for B in B)
def PR(A):return type(A)(B for A in A for B in A)
def Q(A):return max(A for(A,B)in J(A))
def W(A):return max(A for(B,A)in J(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def ZM(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def K(A):return min(A for(B,A)in J(A))
def V(A):return min(A for(A,B)in J(A))
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def ZP(A):return PM(A),PK(A)
def P(A,B):
	C=set();K=U(B);D,E=len(A),len(A[0]);L,M=ZP(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in ZZ(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=_A;break
			if H:C.add((F,G))
	return frozenset(C)
def X(A):return frozenset((A[0],B)for B in range(30))
def M(A):return frozenset((B,A[1])for B in range(30))
def PH(A,B):return ZV(A,L(A),J(B))
def ZS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def PG(A):return V(A)+PM(A)//2,K(A)+PK(A)//2
def PJ(A,B):return ZM(B,G(A),ZP(A))
def ZU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def ZV(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def R(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PS(A,B,C,D):
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
	return ZZ(A,(-V(A),-K(A)))
def ZZ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PZ(A,B):return frozenset((A,B)for B in J(B))
def G(A):return tuple(map(min,zip(*J(A))))
def PU(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PK(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PW(A,B):return PR(ZX(A,B))
def ZY(A,a,b):return lambda x:A(a(x),b(x))
def ZJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PE(A,B):return lambda x:A(B(x))
def PY(A,a,b):return a if A else b
def PX(a,b):return a,b
def PP(A):return frozenset({A})
def PV(A,B):return min(A,key=B)
def ZL(A):return len(A)
def PL(a,b):return type(a)((*a,*b))
def H(a,b):return a==b
def PQ(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def ZW(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));S=PS(I,_A,_A,True);B=PV(S,ZL);T=U(B);V=PM(B);W=PK(B);C=H(V,5);D=H(W,5);Y=PX(C,D);Z=ZW((1,1),Y);a=PQ(Z);E=PG(B);b=ZS(I,E);c=PY(C,(-1,0),(0,1));d=ZW(c,E);e=ZS(I,d);f=PX(b,(0,0));F=PP(f);A=PH(I,B);J=L(A);g=PU(A,J);h=P(A,F);i=PS(A,_A,_A,True);j=ZE(P,F);K=ZE(PJ,A);N=PE(j,K);k=ZJ(PW,M);l=ZJ(PW,X);O=PE(k,N);Q=PE(l,N);m=PY(C,O,Q);n=PY(D,Q,O);o=ZY(PL,m,n);p=ZJ(PZ,e);q=PE(p,o);r=ZY(ZU,K,q);s=PE(R,r);t=ZY(ZZ,s,G);u=PW(t,i);v=ZU(A,u);w=ZZ(T,a);x=ZJ(ZZ,w);y=PW(x,h);z=ZU(v,y);A0=ZV(z,J,g);return[*map(list,A0)]