def PP(A,B):return type(A)(A for A in A if B(A))
def PH(A):return type(A)(B for A in A for B in A)
def V(A):return max(A for(B,A)in U(A))
def W(A):return min(A for(B,A)in U(A))
def ZJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return S(A)|J(A)
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A):return max(A for(A,B)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-Y(A)+1
def PS(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def ZM(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def G(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in U(A)if 0<=A<D and 0<=C<E)
def ZZ(A):return PR(A)==len(A)and PM(A)==1
def ZE(A):return PM(A)==len(A)and PR(A)==1
def H(A,B,C,D):
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
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PJ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def Z(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def PR(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-W(A)+1
def K(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def PQ(A,B):return PH(ZL(A,B))
def ZL(A,B):return type(B)(A(B)for B in B)
def ZV(A,a,b):return lambda x:A(a(x),b(x))
def ZU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def ZP(h,g,f):return lambda x:h(g(f(x)))
def PE(A,B):return lambda x:A(B(x))
def PK(A,B):return B.union(frozenset({A}))
def PU(A,B):return PH(PP(A,B))
def PG(j):return 0,j
def PV(i):return i,0
def PW(a,b):return a or b
def ZW(a,b):return a and b
def R(A):return frozenset({A})
def PY(A,B):return max(A,key=B)
def PL(A,B):return B(max(A,key=B,default=0))
def ZY(A):return len(A)
def PZ(a,b):return a>b
def PX(a,b):return type(a)((*a,*b))
def ZS(n):return n//2 if isinstance(n,int)else(n[0]//2,n[1]//2)
def Q(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def ZQ(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):J=False;I=tuple(map(tuple,I));A=PJ(I,2);L=K(PS,A,A);M=ZU(PZ,6);N=PE(M,ZY);O=ZV(PW,ZE,ZZ);T=ZV(ZW,N,O);V=PU(L,T);B=ZM(I,2,V);W=H(B,True,J,J);C=P(W,2);X=PL(C,PR);D=ZS(X);E=PV(D);F=PG(D);Y=ZX(ZQ,(0,2));a=ZX(ZQ,(2,0));b=ZX(Q,(0,2));c=ZX(Q,(2,0));d=ZX(Z,2);e=ZX(G,B);f=PE(R,Y);g=ZV(PK,a,f);h=ZV(PK,b,g);i=ZV(PK,c,h);j=ZV(PX,S,i);k=ZP(d,e,j);l=ZX(PY,k);m=PE(l,U);n=ZL(m,C);o=ZX(ZQ,E);p=ZX(Q,E);q=ZX(ZQ,F);r=ZX(Q,F);s=ZV(PS,o,p);t=ZV(PS,q,r);u=ZV(PX,s,t);v=PQ(u,n);w=ZM(B,8,v);x=ZM(w,2,A);return[*map(list,x)]